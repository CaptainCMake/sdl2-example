import argparse
import os


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--project", help="Path to the Xcode project", required=True)
    parser.add_argument("--folderPath", help="Path to the folder reference", required=True)
    parser.add_argument("--target", help="Build target name", required=True)
    command_args = parser.parse_args()
    
    with open(command_args.project) as f:
        project_data = f.read()
        
    folder_path = command_args.folderPath
    folder = os.path.basename(folder_path)
    
    id1 = "101"
    id2 = "201"
    
    pbxbuildfile_header = '/* Begin PBXBuildFile section */'
    project_data = project_data.replace(
        pbxbuildfile_header,
        '{0}\n\t\t{1} /* {2} in Resources */ = {{isa = PBXBuildFile; fileRef = {3} /* {2} */; }};'.format(pbxbuildfile_header, id1, folder, id2),
    )
    
    pbxfilereference_header = '/* Begin PBXFileReference section */'
    project_data = project_data.replace(
        pbxfilereference_header,
        '{0}\n\t\t{1} /* {2} */ = {{isa = PBXFileReference; lastKnownFileType = folder.assetcatalog; name = {2}; path = {3}; sourceTree = "<group>"; }};'.format(pbxfilereference_header, id2, folder, folder_path)
    )
    
    pbxgroup_section = '/* Resources */ = {\n\t\t\tisa = PBXGroup;\n\t\t\tchildren = ('
    project_data = project_data.replace(
        pbxgroup_section,
        '{0}\n\t\t\t\t{1} /* {2} */,'.format(pbxgroup_section, id2, folder)
    )
    
    pbxbuildphase_section = 'isa = PBXResourcesBuildPhase;\n\t\t\tbuildActionMask = 2147483647;\n\t\t\tfiles = ('
    project_data = project_data.replace(
        pbxbuildphase_section,
        '{0}\n\t\t\t\t{1} /* {2} in Resources */,'.format(pbxbuildphase_section, id1, folder)
    )
        
    with open(command_args.project, "w") as f:
        f.write(project_data)      


if __name__ == "__main__":
    main()
