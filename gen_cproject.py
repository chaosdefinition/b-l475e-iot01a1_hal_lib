#!/usr/bin/env python2

import os
import sys


#
# Path to our Clang.
#
clang_path = '${HOME}/projects/silhouette/llvm-build/bin/clang'

#
# Project name.
#
project_name = 'b-l475e-iot01a1_hal_lib'

#
# Dict of boards we use.
#
boards = {
    'B-L475E-IOT01A1': {
        'mcu': 'STM32L475VGTx',
    }
}

#
# Dict of dependent libraries.
#
libraries = {
    'c': {
        'includes': [
            '${openstm32_compiler_path}/../arm-none-eabi/include',
        ],
    },
}


#
# Dict of programs to compile.
#
programs = {
    'b-l475e-iot01a1_hal_lib': {
        'defines': [
            'STM32L475xx',
            'USE_HAL_DRIVER',
        ],
        'includes': [
            '${ProjDirPath}/Utilities/Components/m24sr',
            '${ProjDirPath}/Utilities/Components/cs43l22',
            '${ProjDirPath}/Utilities/Components/hx8347i',
            '${ProjDirPath}/Utilities/Components/mx25lm51245g',
            '${ProjDirPath}/Utilities/Components/mfxstm32l152',
            '${ProjDirPath}/CMSIS/device',
            '${ProjDirPath}/Utilities/Components/cs42l51',
            '${ProjDirPath}/Utilities/Components/n25q128a',
            '${ProjDirPath}/Utilities/Components/st7735',
            '${ProjDirPath}/Utilities/Components/ft3x67',
            '${ProjDirPath}/Utilities/Components/rk043fn48h',
            '${ProjDirPath}/Utilities/Components/hx8347g',
            '${ProjDirPath}/HAL_Driver/Inc/Legacy',
            '${ProjDirPath}/Utilities/Components/ov9655',
            '${ProjDirPath}/Utilities/Components/stmpe1600',
            '${ProjDirPath}/Utilities/Components/Common',
            '${ProjDirPath}/Utilities/Components/l3gd20',
            '${ProjDirPath}/Utilities/Components/lsm6dsl',
            '${ProjDirPath}/HAL_Driver/Inc',
            '${ProjDirPath}/Utilities/Components/stmpe811',
            '${ProjDirPath}/Utilities/Components/wm8994',
            '${ProjDirPath}/Utilities/B-L475E-IOT01',
            '${ProjDirPath}/Utilities/Components/ft5336',
            '${ProjDirPath}/Utilities/Components/n25q256a',
            '${ProjDirPath}/Utilities/Components/hts221',
            '${ProjDirPath}/Utilities/Components/ls016b8uy',
            '${ProjDirPath}/Utilities/Components/ft6x06',
            '${ProjDirPath}/Utilities/Components/lis3mdl',
            '${ProjDirPath}/Utilities/Components/lps22hb',
            '${ProjDirPath}/Utilities/Components/st7789h2',
            '${ProjDirPath}/Utilities/Components/lsm303c',
            '${ProjDirPath}/Utilities/Components/iss66wvh8m8',
            '${ProjDirPath}/Utilities/Components/lsm303dlhc',
            '${ProjDirPath}/CMSIS/core',
            '${ProjDirPath}/Utilities/Components/mx25r6435f',
        ],
        'directories': {
            'CMSIS': '',
            'HAL_Driver': '',
            'Utilities': '',
        },
    },
}


#
# Dict of configurations.
#
configurations = {
    'baseline': {
        'cflags': [
            '--target=arm-none-eabi',
        ],
        'ldflags': [
            '-fuse-ld=lld',
            '--target=arm-none-eabi',
        ],
    },
}

###############################################################################

#
# Generate and return the cproject header.
#
def gen_header():
    xml =  '<?xml version="1.0" encoding="UTF-8" standalone="no"?>\n'
    xml += '<?fileVersion 4.0.0?>\n'
    xml += '<cproject storage_type_id="org.eclipse.cdt.core.XmlProjectDescriptionStorage">\n'
    return xml


#
# Generate and return the cproject footer.
#
def gen_footer():
    xml =  '  <storageModule moduleId="cdtBuildSystem" version="4.0.0">\n'
    xml += '    <project id="' + project_name + '.null" name="' + project_name + '"/>\n'
    xml += '  </storageModule>\n'
    xml += '  <storageModule moduleId="org.eclipse.cdt.core.LanguageSettingsProviders"/>\n'
    xml += '</cproject>\n'
    return xml


#
# Generate and return the header of scanner configurations.
#
def gen_scanner_header():
    xml =  '  <storageModule moduleId="scannerConfiguration">\n'
    xml += '    <autodiscovery enabled="false" problemReportingEnabled="false" selectedProfileId=""/>\n'
    return xml


#
# Generate and return the scanner configuration for a given program.
#
# @program: the name of the program.
#
def gen_scanner_config(program):
    program_id = programs[program]['id']
    xml =  '    <scannerConfigBuildInfo instanceId="fr.ac6.managedbuild.config.gnu.cross.lib.release.' + program_id + ';fr.ac6.managedbuild.config.gnu.cross.lib.release.' + program_id + '.;fr.ac6.managedbuild.tool.gnu.cross.c.compiler.' + program_id + ';fr.ac6.managedbuild.tool.gnu.cross.c.compiler.input.c.' + program_id + '">\n'
    xml += '      <autodiscovery enabled="false" problemReportingEnabled="false" selectedProfileId=""/>\n'
    xml += '    </scannerConfigBuildInfo>\n'
    return xml


#
# Generate and return the footer of scanner configurations.
#
def gen_scanner_footer():
    return '  </storageModule>\n'


#
# Generate and return the header of core settings.
#
def gen_core_settings_header():
    return '  <storageModule moduleId="org.eclipse.cdt.core.settings">\n'


#
# Generate and return the core setting for a given program.
#
# @board: the name of the board to use.
# @conf: the name of the configuration to use.
# @program: the name of the program.
#
def gen_core_settings_config(board, conf, program):
    program_id = programs[program]['id']

    xml =  '    <!-- Configuration of ' + program + ' -->\n'
    xml += '    <cconfiguration id="fr.ac6.managedbuild.config.gnu.cross.lib.release.' + program_id + '">\n'
    xml += '      <storageModule buildSystemId="org.eclipse.cdt.managedbuilder.core.configurationDataProvider" id="fr.ac6.managedbuild.config.gnu.cross.lib.release.' + program_id + '" moduleId="org.eclipse.cdt.core.settings" name="' + program + '">\n'
    xml += '        <externalSettings>\n'
    xml += '          <externalSetting>\n'
    xml += '            <entry flags="VALUE_WORKSPACE_PATH" kind="includePath" name="/' + program + '"/>\n'
    xml += '            <entry flags="VALUE_WORKSPACE_PATH" kind="libraryPath" name="/' + program + '/' + program + '"/>\n';
    xml += '            <entry flags="RESOLVED" kind="libraryFile" name="' + program + '" srcPrefixMapping="" srcRootPath=""/>\n'
    xml += '          </externalSetting>\n'
    xml += '        </externalSettings>\n'
    xml += '        <extensions>\n'
    xml += '          <extension id="org.eclipse.cdt.core.ELF" point="org.eclipse.cdt.core.BinaryParser"/>\n'
    xml += '          <extension id="org.eclipse.cdt.core.GASErrorParser" point="org.eclipse.cdt.core.ErrorParser"/>\n'
    xml += '          <extension id="org.eclipse.cdt.core.GmakeErrorParser" point="org.eclipse.cdt.core.ErrorParser"/>\n'
    xml += '          <extension id="org.eclipse.cdt.core.CWDLocator" point="org.eclipse.cdt.core.ErrorParser"/>\n'
    xml += '          <extension id="org.eclipse.cdt.core.GCCErrorParser" point="org.eclipse.cdt.core.ErrorParser"/>\n'
    xml += '        </extensions>\n'
    xml += '      </storageModule>\n'
    xml += '      <storageModule moduleId="cdtBuildSystem" version="4.0.0">\n'
    xml += '        <configuration artifactExtension="a" artifactName="${ConfigName}" buildArtefactType="org.eclipse.cdt.build.core.buildArtefactType.staticLib" buildProperties="org.eclipse.cdt.build.core.buildArtefactType=org.eclipse.cdt.build.core.buildArtefactType.staticLib,org.eclipse.cdt.build.core.buildType=org.eclipse.cdt.build.core.buildType.release" cleanCommand="rm -rf" description="" id="fr.ac6.managedbuild.config.gnu.cross.lib.release.' + program_id + '" name="' + program + '" optionalBuildProperties="org.eclipse.cdt.docker.launcher.containerbuild.property.selectedvolumes=,org.eclipse.cdt.docker.launcher.containerbuild.property.volumes=" parent="fr.ac6.managedbuild.config.gnu.cross.lib.release">\n'
    xml += '          <folderInfo id="fr.ac6.managedbuild.config.gnu.cross.lib.release.' + program_id + '." name="/" resourcePath="">\n'
    xml += '            <toolChain id="fr.ac6.managedbuild.toolchain.gnu.cross.lib.release.' + program_id + '" name="Ac6 STM32 MCU GCC" superClass="fr.ac6.managedbuild.toolchain.gnu.cross.lib.release">\n'
    xml += '              <option id="fr.ac6.managedbuild.option.gnu.cross.mcu.' + program_id + '" name="Mcu" superClass="fr.ac6.managedbuild.option.gnu.cross.mcu" value="' + boards[board]['mcu'] + '" valueType="string"/>\n'
    xml += '              <option id="fr.ac6.managedbuild.option.gnu.cross.fpu.' + program_id + '" name="Floating point hardware" superClass="fr.ac6.managedbuild.option.gnu.cross.fpu" value="fr.ac6.managedbuild.option.gnu.cross.fpu.fpv4-sp-d16" valueType="enumerated"/>\n'
    xml += '              <option id="fr.ac6.managedbuild.option.gnu.cross.floatabi.' + program_id + '" name="Floating-point ABI" superClass="fr.ac6.managedbuild.option.gnu.cross.floatabi" value="fr.ac6.managedbuild.option.gnu.cross.floatabi.hard" valueType="enumerated"/>\n'
    xml += '              <option id="fr.ac6.managedbuild.option.gnu.cross.board.' + program_id + '" name="Board" superClass="fr.ac6.managedbuild.option.gnu.cross.board" value="' + board + '" valueType="string"/>\n'
    xml += '              <option id="fr.ac6.managedbuild.option.gnu.cross.prefix.' + program_id + '" name="Prefix" superClass="fr.ac6.managedbuild.option.gnu.cross.prefix" value="" valueType="string"/>\n'
    xml += '              <targetPlatform archList="all" binaryParser="org.eclipse.cdt.core.ELF" id="fr.ac6.managedbuild.targetPlatform.gnu.cross.' + program_id + '" isAbstract="false" osList="all" superClass="fr.ac6.managedbuild.targetPlatform.gnu.cross"/>\n'
    xml += '              <builder buildPath="${workspace_loc:/' + project_name + '}/Release" id="fr.ac6.managedbuild.builder.gnu.cross.' + program_id + '" keepEnvironmentInBuildfile="false" managedBuildOn="true" name="Gnu Make Builder" parallelBuildOn="true" parallelizationNumber="optimal" superClass="fr.ac6.managedbuild.builder.gnu.cross"/>\n'
    ###########################################################################
    # Set up C compiler
    ###########################################################################
    xml += '              <tool command="' + clang_path + '" id="fr.ac6.managedbuild.tool.gnu.cross.c.compiler.' + program_id + '" name="MCU GCC Compiler" superClass="fr.ac6.managedbuild.tool.gnu.cross.c.compiler">\n'
    xml += '                <option id="fr.ac6.managedbuild.gnu.c.compiler.option.optimization.level.' + program_id + '" name="Optimization Level" superClass="fr.ac6.managedbuild.gnu.c.compiler.option.optimization.level" useByScannerDiscovery="false" value="fr.ac6.managedbuild.gnu.c.optimization.level.most" valueType="enumerated"/>\n'
    xml += '                <option defaultValue="gnu.c.debugging.level.none" id="gnu.c.compiler.option.debugging.level.' + program_id + '" name="Debug Level" superClass="gnu.c.compiler.option.debugging.level" useByScannerDiscovery="false" valueType="enumerated"/>\n'
    # Add macro definitions
    xml += '                <option IS_BUILTIN_EMPTY="false" IS_VALUE_EMPTY="false" id="gnu.c.compiler.option.preprocessor.def.symbols.' + program_id + '" name="Defined symbols (-D)" superClass="gnu.c.compiler.option.preprocessor.def.symbols" useByScannerDiscovery="false" valueType="definedSymbols">\n'
    if 'defines' in boards[board]:
        for define in boards[board]['defines']:
            xml += '                  <listOptionValue builtIn="false" value="' + define + '"/>\n'
    for library in libraries:
        if 'defines' in libraries[library]:
            for define in libraries[library]['defines']:
                xml += '                  <listOptionValue builtIn="false" value="' + define + '"/>\n'
    if 'defines' in configurations[conf]:
        for define in configurations[conf]['defines']:
            xml += '                  <listOptionValue builtIn="false" value="' + define + '"/>\n'
    if 'defines' in programs[program]:
        for define in programs[program]['defines']:
            xml += '                  <listOptionValue builtIn="false" value="' + define + '"/>\n'
    xml += '                </option>\n'
    # Add include paths
    xml += '                <option IS_BUILTIN_EMPTY="false" IS_VALUE_EMPTY="false" id="gnu.c.compiler.option.include.paths.' + program_id + '" name="Include paths (-I)" superClass="gnu.c.compiler.option.include.paths" useByScannerDiscovery="false" valueType="includePath">\n'
    if 'includes' in boards[board]:
        for include in boards[board]['includes']:
            xml += '                  <listOptionValue builtIn="false" value="&quot;' + include + '&quot;"/>\n'
    for library in libraries:
        if 'includes' in libraries[library]:
            for include in libraries[library]['includes']:
                xml += '                  <listOptionValue builtIn="false" value="&quot;' + include + '&quot;"/>\n'
    if 'includes' in configurations[conf]:
        for include in configurations[conf]["includes"]:
            xml += '                  <listOptionValue builtIn="false" value="&quot;' + include + '&quot;"/>\n'
    if 'includes' in programs[program]:
        for include in programs[program]['includes']:
            xml += '                  <listOptionValue builtIn="false" value="&quot;' + include + '&quot;"/>\n'
    xml += '                </option>\n'
    # Add other C flags
    xml += '                <option id="fr.ac6.managedbuild.gnu.c.compiler.option.misc.other.' + program_id + '" name="Other flags" superClass="fr.ac6.managedbuild.gnu.c.compiler.option.misc.other" useByScannerDiscovery="false" value="'
    if 'cflags' in boards[board]:
        for cflag in boards[board]['cflags']:
            xml += cflag + ' '
    for library in libraries:
        if 'cflags' in libraries[library]:
            for cflag in libraries[library]['cflags']:
                xml += cflag + ' '
    if 'cflags' in configurations[conf]:
        for cflag in configurations[conf]['cflags']:
            xml += cflag + ' '
    if 'cflags' in programs[program]:
        for cflag in programs[program]['cflags']:
            xml += cflag + ' '
    xml += '" valueType="string"/>\n'
    xml += '                <option id="gnu.c.compiler.option.dialect.std.' + program_id + '" name="Language standard" superClass="gnu.c.compiler.option.dialect.std" useByScannerDiscovery="true" value="gnu.c.compiler.dialect.default" valueType="enumerated"/>\n'
    xml += '                <inputType id="fr.ac6.managedbuild.tool.gnu.cross.c.compiler.input.c.' + program_id + '" superClass="fr.ac6.managedbuild.tool.gnu.cross.c.compiler.input.c"/>\n'
    xml += '                <inputType id="fr.ac6.managedbuild.tool.gnu.cross.c.compiler.input.s.' + program_id + '" superClass="fr.ac6.managedbuild.tool.gnu.cross.c.compiler.input.s"/>\n'
    xml += '              </tool>\n'
    ###########################################################################
    # Set up C++ compiler
    ###########################################################################
    xml += '              <tool id="fr.ac6.managedbuild.tool.gnu.cross.cpp.compiler.' + program_id + '" name="MCU G++ Compiler" superClass="fr.ac6.managedbuild.tool.gnu.cross.cpp.compiler">\n'
    xml += '                <option id="fr.ac6.managedbuild.gnu.cpp.compiler.option.optimization.level.' + program_id + '" name="Optimization Level" superClass="fr.ac6.managedbuild.gnu.cpp.compiler.option.optimization.level" useByScannerDiscovery="false" value="fr.ac6.managedbuild.gnu.cpp.optimization.level.most" valueType="enumerated"/>\n'
    xml += '                <option defaultValue="gnu.cpp.compiler.debugging.level.none" id="gnu.cpp.compiler.option.debugging.level.' + program_id + '" name="Debug Level" superClass="gnu.cpp.compiler.option.debugging.level" useByScannerDiscovery="false" valueType="enumerated"/>\n'
    xml += '              </tool>\n'
    ###########################################################################
    # Set up C linker
    ###########################################################################
    xml += '              <tool id="fr.ac6.managedbuild.tool.gnu.cross.c.linker.' + program_id + '" name="MCU GCC Linker" superClass="fr.ac6.managedbuild.tool.gnu.cross.c.linker"/>\n'
    ###########################################################################
    # Set up C++ linker
    ###########################################################################
    xml += '              <tool id="fr.ac6.managedbuild.tool.gnu.cross.cpp.linker.' + program_id + '" name="MCU G++ Linker" superClass="fr.ac6.managedbuild.tool.gnu.cross.cpp.linker"/>\n'
    ###########################################################################
    # Set up archiver
    ###########################################################################
    xml += '              <tool id="fr.ac6.managedbuild.tool.gnu.archiver.' + program_id + '" name="MCU GCC Archiver" superClass="fr.ac6.managedbuild.tool.gnu.archiver"/>\n'
    ###########################################################################
    # Set up assembler
    ###########################################################################
    xml += '              <tool command="' + clang_path + '" id="fr.ac6.managedbuild.tool.gnu.cross.assembler.lib.release.' + program_id + '" name="MCU GCC Assembler" superClass="fr.ac6.managedbuild.tool.gnu.cross.assembler.lib.release">\n'
    # Add include paths
    xml += '                <option IS_BUILTIN_EMPTY="false" IS_VALUE_EMPTY="false" id="gnu.both.asm.option.include.paths.' + program_id + '" name="Include paths (-I)" superClass="gnu.both.asm.option.include.paths" useByScannerDiscovery="false" valueType="includePath">\n'
    if 'includes' in boards[board]:
        for include in boards[board]['includes']:
            xml += '                  <listOptionValue builtIn="false" value="&quot;' + include + '&quot;"/>\n'
    for library in libraries:
        if 'includes' in libraries[library]:
            for include in libraries[library]['includes']:
                xml += '                  <listOptionValue builtIn="false" value="&quot;' + include + '&quot;"/>\n'
    if 'includes' in configurations[conf]:
        for include in configurations[conf]["includes"]:
            xml += '                  <listOptionValue builtIn="false" value="&quot;' + include + '&quot;"/>\n'
    if 'includes' in programs[program]:
        for include in programs[program]['includes']:
            xml += '                  <listOptionValue builtIn="false" value="&quot;' + include + '&quot;"/>\n'
    xml += '                </option>\n'
    xml += '                <inputType id="cdt.managedbuild.tool.gnu.assembler.input.' + program_id + '" superClass="cdt.managedbuild.tool.gnu.assembler.input"/>\n'
    xml += '                <inputType id="fr.ac6.managedbuild.tool.gnu.cross.assembler.input.' + program_id + '" superClass="fr.ac6.managedbuild.tool.gnu.cross.assembler.input"/>\n'
    xml += '              </tool>\n'
    xml += '            </toolChain>\n'
    xml += '          </folderInfo>\n'
    ###########################################################################
    # Set up source entries
    ###########################################################################
    xml += '          <sourceEntries>\n'
    if 'directories' in boards[board]:
        for directory in boards[board]['directories']:
            xml += '            <entry excluding="' + boards[board]['directories'][directory] + '" flags="VALUE_WORKSPACE_PATH|RESOLVED" kind="sourcePath" name="' + directory + '"/>\n'
    if 'directories' in programs[program]:
        for directory in programs[program]['directories']:
            xml += '            <entry excluding="' + programs[program]['directories'][directory] + '" flags="VALUE_WORKSPACE_PATH|RESOLVED" kind="sourcePath" name="' + directory + '"/>\n'
    xml += '          </sourceEntries>\n'
    xml += '        </configuration>\n'
    xml += '      </storageModule>\n'
    xml += '      <storageModule moduleId="org.eclipse.cdt.core.externalSettings"/>\n'
    xml += '    </cconfiguration>\n'

    return xml


#
# Generate and return the footer of core settings.
#
def gen_core_settings_footer():
    return '  </storageModule>\n'


#
# Generate and return the whole cproject file content for the given board and
# configuration.
#
# @board: the name of the board to use.
# @conf: the name of the configuration to use.
#
def gen_cproject(board, conf):
    xml =  gen_header()

    # Generate core settings for each program
    xml += gen_core_settings_header()
    for program in sorted(programs.keys()):
        xml += gen_core_settings_config(board, conf, program)
    xml += gen_core_settings_footer()

    # Generate scanner configuration for each program
    xml += gen_scanner_header()
    for program in sorted(programs.keys()):
        xml += gen_scanner_config(program)
    xml += gen_scanner_footer()

    xml += gen_footer()

    return xml


#
# Generate and return the file content of language.settings.xml which disables
# discovering compiler's built-in language settings.
#
def gen_language_settings():
    xml  = '<?xml version="1.0" encoding="UTF-8" standalone="no"?>\n'
    xml += '<project>\n'
    for program in sorted(programs.keys()):
        xml += '  <configuration id="fr.ac6.managedbuild.config.gnu.cross.lib.release.' + programs[program]['id'] + '" name="' + program + '">\n'
        xml += '    <extension point="org.eclipse.cdt.core.LanguageSettingsProvider">\n'
        xml += '      <provider copy-of="extension" id="org.eclipse.cdt.ui.UserLanguageSettingsProvider"/>\n'
        xml += '      <provider-reference id="org.eclipse.cdt.core.ReferencedProjectsLanguageSettingsProvider" ref="shared-provider"/>\n'
        xml += '      <provider-reference id="org.eclipse.cdt.managedbuilder.core.MBSLanguageSettingsProvider" ref="shared-provider"/>\n'
        xml += '    </extension>\n'
        xml += '  </configuration>\n'
    xml += '</project>\n'

    return xml


#
# Print out the usage string.
#
def usage():
    us  = 'Usage: python ' + sys.argv[0] + ' [options]\n\n'
    us += 'Options:\n'
    us += '  -b board       specify the board to use (default STM32F469I-DISCO)\n'
    print us


#
# The main function.
#
def main():
    # Assign an ID to each program
    program_id = 0
    for program in sorted(programs.keys()):
        programs[program]['id'] = str(program_id)
        program_id += 1

    # Parse command-line arguments
    board = 'B-L475E-IOT01A1'
    args = iter(sys.argv[1:])
    for arg in args:
        if arg == '-b':
            board = args.next()
        else:
            usage()
            sys.exit(1)
    if not board in boards:
        print 'Unknow board: ' + board
        print 'Supported boards are: ', boards.keys()
        sys.exit(1)

    # Generate cproject file for each configuration
    for conf in configurations:
        conf_filename = 'cproject_' + conf
        xml = gen_cproject(board, conf)
        with open(conf_filename, 'w') as f:
            f.write(xml)

    # In addition, also generate language.settings.xml that disable discovering
    # compiler's built-in language settings
    if not os.path.isdir('.settings'):
        os.mkdir('.settings')
    with open('.settings/language.settings.xml', 'w') as f:
        f.write(gen_language_settings())


if __name__ == '__main__':
    main()
