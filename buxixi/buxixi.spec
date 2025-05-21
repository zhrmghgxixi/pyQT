# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['F:\\Document_File\\Various_Documents\\pyQT\\buxixi\\buxixi (3)\\buxixi.py'],
             pathex=[],
             binaries=[],
             datas=[('F:\\Document_File\\Various_Documents\\pyQT\\buxixi\\buxixi (3)\\Ui_buxixi.py', '.')],
             hiddenimports=[],
             hookspath=[],
             hooksconfig={},
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,  
          [],
          name='buxixi',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False,
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None , icon='F:\\Document_File\\Various_Documents\\pyQT\\buxixi\\buxixi (3)\\img\\xixi.ico')
