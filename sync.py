#!/usr/bin/env python3
import os
import re
import shutil
import argparse
import urllib.parse
from pathlib import Path
from collections import defaultdict
# Regex patterns for Obsidian links
# Matches [[Link]], [[Link|Alias]], [[Link#Header]], ![[Image.png]]
WIKILINK_RE = re.compile(r'(?:!|)\[\[(.*?)\]\]')
# Matches [Text](Link), ![Text](Image.png)
MDLINK_RE = re.compile(r'(?:!|)\[.*?\]\((.*?)\)')
class ObsidianSync:
    def __init__(self, vault_dir, output_dir):
        self.vault_dir = Path(vault_dir).resolve()
        self.output_dir = Path(output_dir).resolve()
        self.file_index = self._build_index()
        self.processed_files = set()
        self.queue = set()
    def _build_index(self):
        """
        Builds a map of lowercased filenames to their relative paths in the vault.
        Obsidian wikilinks often just use the filename without the path.
        """
        index = defaultdict(list)
        print("Building vault index...")
        for root, dirs, files in os.walk(self.vault_dir):
            # Ignore hidden directories like .obsidian, .git, .trash
            dirs[:] = [d for d in dirs if not d.startswith('.')]
            for file in files:
                if file.startswith('.'):
                    continue
                full_path = Path(root) / file
                rel_path = full_path.relative_to(self.vault_dir)
                # Store by name for wikilink resolution
                index[file.lower()].append(rel_path)
                # Also store without extension for markdown files
                if file.lower().endswith('.md'):
                    index[file[:-3].lower()].append(rel_path)
        return index
    def _resolve_link(self, link_target, current_file_rel_path):
        """
        Attempts to find the actual relative path of a linked file.
        """
        link_target = urllib.parse.unquote(link_target)
        
        # Clean up wikilink extras (aliases, headers)
        link_target = link_target.split('|')[0]
        link_target = link_target.split('#')[0]
        
        if not link_target.strip():
            return None
            
        # Ignore external URLs
        if link_target.startswith(('http://', 'https://', 'mailto:', 'obsidian://')):
            return None
        # 1. Try exact relative path (from current file's directory)
        current_dir = (self.vault_dir / current_file_rel_path).parent
        exact_path = (current_dir / link_target).resolve()
        if exact_path.is_file() and exact_path.is_relative_to(self.vault_dir):
            return exact_path.relative_to(self.vault_dir)
        # 2. Try root relative path
        root_path = (self.vault_dir / link_target).resolve()
        if root_path.is_file() and root_path.is_relative_to(self.vault_dir):
            return root_path.relative_to(self.vault_dir)
        # 3. Search in index (Obsidian default behavior)
        target_lower = link_target.lower()
        if target_lower in self.file_index:
            # If multiple files have the same name, we pick the first one (or could prioritize closest)
            return self.file_index[target_lower][0]
        return None
    def _extract_links(self, file_path):
        """Reads a markdown file and yields all resolved links."""
        try:
            with open(self.vault_dir / file_path, 'r', encoding='utf-8') as f:
                content = f.read()
        except Exception as e:
            print(f"Error reading {file_path}: {e}")
            return []
        links = set()
        
        # Extract wikilinks
        for match in WIKILINK_RE.finditer(content):
            links.add(match.group(1))
            
        # Extract markdown links
        for match in MDLINK_RE.finditer(content):
            links.add(match.group(1))
        resolved_paths = set()
        for link in links:
            resolved = self._resolve_link(link, file_path)
            if resolved:
                resolved_paths.add(resolved)
            else:
                # print(f"  [Warning] Could not resolve link: '{link}' in '{file_path}'")
                pass
        return resolved_paths
    def _copy_file(self, rel_path):
        """Copies a file from vault to output directory preserving folder structure."""
        src = self.vault_dir / rel_path
        dst = self.output_dir / rel_path
        
        if not src.exists():
            return False
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dst)
        return True
    def sync_note(self, note_name):
        """Main entry point to sync a note and all its dependencies."""
        resolved = self._resolve_link(note_name, Path('.'))
        if not resolved:
            print(f"Could not find note: {note_name}")
            return
        self.queue.add(resolved)
        
        print(f"\nStarting sync for: {resolved}")
        
        while self.queue:
            current_path = self.queue.pop()
            
            if current_path in self.processed_files:
                continue
                
            self.processed_files.add(current_path)
            
            if self._copy_file(current_path):
                print(f"Copied: {current_path}")
                
                # Only extract links if it's a markdown file
                if current_path.suffix.lower() == '.md':
                    dependencies = self._extract_links(current_path)
                    for dep in dependencies:
                        if dep not in self.processed_files:
                            self.queue.add(dep)
        print(f"\nSync complete. Processed {len(self.processed_files)} files.")
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Sync Obsidian notes and their dependencies to Quartz.')
    parser.add_argument('note', help='Name or relative path of the note to sync (e.g., "My Note" or "folder/note.md")')
    parser.add_argument('--vault', default='/home/ixdire/Water/Fire', help='Path to Obsidian vault')
    parser.add_argument('--out', default='/home/ixdire/Water/crap/quartz/content', help='Path to Quartz content directory')
    
    args = parser.parse_args()
    
    syncer = ObsidianSync(args.vault, args.out)
    syncer.sync_note(args.note)
