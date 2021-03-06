
PyOpenGLとPyOpenGL_accelerate
=================================

PyOpenGLは標準的なpipを使用してPyPI経由で通常配布されます::

    $ pip install PyOpenGL PyOpenGL_accelerate

このリポジトリは、ブランチング/クローニングと実行によってインストールできます
setup.py ::

    $ cd pyopengl
    $ python setup.py develop
    $ cd accelerate
    $ python setup.py develop

PyOpenGL_accelerateをコンパイルするには、
機能するPython拡張コンパイル環境。

PyOpenGLを学ぶ
-----------------

PyOpenGLを初めてお使いの方は、OpenGLContextのチュートリアルページから始めたいと思うでしょう。
これらのチュートリアルではOpenGLContextが必要です（これは大きなラッパーです
シーングラフエンジン、VRML97パーサ、多くのデモなど）をインストールするには::

    $ pip install "OpenGLContext-full == 3.1.1

`ドキュメンテーションページ`は、以下のようなパラメータと意味を調べるのに便利です。
PyOpenGLが呼び出します。

.. _`tutorial page`：http://pyopengl.sourceforge.net/context/tutorials/index.html
.. _`documentation pages`：http://pyopengl.sourceforge.net/documentation/


テストの実行
--------------
テストの実行
--------------

テストスイートを実行するには、Pygameを事前にビルドしておき、
ナンシーホイール、Python 2.6,2.7,3.4、3.5。ザ
テストスイート用のホイールは、ディレクトリに格納する必要があります
ルートチェックアウトと同じレベルの「ホイールハウス」と呼ばれています。

Ubuntuでホイールを構築する::

    $ hgクローンhttps://bitbucket.org/pygame/pygame
    $ apt-get build-dep pygame python-numpy
    $ pip2.6 wheel / pygame numpy
    $ pip2.7 wheel / pygame numpy
    $ pip3.4 wheel / pygame numpy
    $ pip3.5 wheel / pygame numpy

pyopenglをチェックアウトしたのと同じディレクトリ
ディレクトリにあなたのすべての車輪がありますpyopengl
toxスイートが期待しています。

あなたは明らかにtoxを実行するために `tox`がインストールされている必要があります。
このような：：

    $ tox

その結果、多数のテストが環境のマトリックスで実行されているため、
Pythonのバージョン：

    * 2.7
    * 2.6
    * 3.4

アクセラレーションモジュールの有無にかかわらずテストを行い、
環境にnumpyをインストールしないでください。 Python 3.5は
しかし、Ubuntuのsite.pyには何か不具合があります
毒性の下で試験が実行されることを防ぎます。






PyOpenGL and PyOpenGL_accelerate
=================================

PyOpenGL is normally distributed via PyPI using standard pip::

    $ pip install PyOpenGL PyOpenGL_accelerate

You can install this repository by branching/cloning and running
setup.py::

    $ cd pyopengl
    $ python setup.py develop
    $ cd accelerate
    $ python setup.py develop

Note that to compile PyOpenGL_accelerate you will need to have 
a functioning Python extension-compiling environment.

Learning PyOpenGL
-----------------

If you are new to PyOpenGL, you likely want to start with the OpenGLContext `tutorial page`_.
Those tutorials require OpenGLContext, (which is a big wrapper including a whole
scenegraph engine, VRML97 parser, lots of demos, etc) you can install that with::

    $ pip install "OpenGLContext-full==3.1.1

The `documentation pages`_ are useful for looking up the parameters and semantics of 
PyOpenGL calls.

.. _`tutorial page`: http://pyopengl.sourceforge.net/context/tutorials/index.html
.. _`documentation pages`: http://pyopengl.sourceforge.net/documentation/


Running Tests
--------------

You can run the test suite only if you have prebuilt Pygame and 
Numpy wheels, along with Python 2.6, 2.7, 3.4 and 3.5. The 
wheels for the test suite to use should be stored in a directory
called "wheelhouse" at the same level as the root checkout here.

To build the wheels on Ubuntu::

    $ hg clone https://bitbucket.org/pygame/pygame
    $ apt-get build-dep pygame python-numpy
    $ pip2.6 wheel ./pygame numpy
    $ pip2.7 wheel ./pygame numpy
    $ pip3.4 wheel ./pygame numpy
    $ pip3.5 wheel ./pygame numpy

if you do that in the same directory where you checked out pyopengl
you will have all of your wheels in the directory the pyopengl 
tox suite is expecting.

You'll obviously need `tox` installed to run tox, which looks
like this::

    $ tox

The result being a lot of tests being run in a matrix of environments,
with Python versions:

    * 2.7
    * 2.6
    * 3.4

Where we test with and without the accelerate module and with and 
without numpy installed in the environment.  Python 3.5 should 
work, but there's something screwy with the Ubuntu site.py that 
prevents the tests running under tox.
