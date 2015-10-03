

from distutils.core import setup, Extension
from glob import glob
import time, sys

mod = Extension(
	'musicplayer',
	sources = glob("*.cpp"),
	depends = glob("*.h") + glob("*.hpp"),
	extra_compile_args = ["-std=c++11"],
	undef_macros = ['NDEBUG'],
	libraries = [
		'avutil',
		'avformat',
		'avcodec',
		'swresample',
		'portaudio',
		'chromaprint'
		]
	)

# Add some more include/lib paths.
# Note: This should probably cover already a lot of cases.
# However, if this is not enough, get some more inspiration from here:
#   https://github.com/python-imaging/Pillow/blob/master/setup.py
def addPrefix(prefix):
	mod.include_dirs += [prefix + "/include"]
	mod.library_dirs += [prefix + "/lib"]
addPrefix("/usr/local")
addPrefix("/opt/local") # e.g. MacPorts
if sys.platform == "darwin": addPrefix("/sw") # fink dir


setup(
	name = 'musicplayer',
	version = time.strftime("1.%Y%m%d.%H%M%S", time.gmtime()),
	description = 'Music player core Python module',
	author = 'Albert Zeyer',
	author_email = 'albzey@gmail.com',
	url = 'https://github.com/albertz/music-player-core',
	license = '2-clause BSD license',
	long_description = open('README.rst').read(),
	classifiers = [
		'Development Status :: 5 - Production/Stable',
		'Environment :: Console',
		'Environment :: MacOS X',
		'Environment :: Win32 (MS Windows)',
		'Environment :: X11 Applications',
		'Intended Audience :: Developers',
		'Intended Audience :: Education',
		'Intended Audience :: End Users/Desktop',
		'License :: OSI Approved :: BSD License',
		'Operating System :: MacOS :: MacOS X',
		'Operating System :: Microsoft :: Windows',
		'Operating System :: POSIX',
		'Operating System :: Unix',
		'Programming Language :: C++',
		'Programming Language :: Python',
		'Topic :: Multimedia :: Sound/Audio',
		'Topic :: Multimedia :: Sound/Audio :: Analysis',
		'Topic :: Multimedia :: Sound/Audio :: Players',
		'Topic :: Multimedia :: Sound/Audio :: Players :: MP3',
		'Topic :: Software Development :: Libraries :: Python Modules',
		],
	ext_modules = [mod]
)

