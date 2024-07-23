'''
Given an absolute path for a Unix-style file system, which begins with a slash '/', transform this path into its simplified canonical path.

In Unix-style file system context, a single period '.' signifies the current directory, a double period ".." denotes moving up one directory level, and multiple slashes such as "//" are interpreted as a single slash. In this problem, treat sequences of periods not covered by the previous rules (like "...") as valid names for files or directories.
'''

class Solution:
    def simplifyPath(self, path: str) -> str:
        dirOrFiles = []
        path = path.split("/")
        for elem in path:
            if dirOrFiles and elem == "..":
                dirOrFiles.pop()
            elif elem not in [".", "", ".."]:
                dirOrFiles.append(elem)
                
        return "/" + "/".join(dirOrFiles)
        