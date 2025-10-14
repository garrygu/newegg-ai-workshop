Conda--> Python 3.12:

(base) C:\Users\ai>conda create -n torch312 python=3.12 -y
3 channel Terms of Service accepted
Retrieving notices: done
Channels:
 - defaults
Platform: win-64
Collecting package metadata (repodata.json): done
Solving environment: done


==> WARNING: A newer version of conda exists. <==
    current version: 25.7.0
    latest version: 25.9.0

Please update conda by running

    $ conda update -n base -c defaults conda



## Package Plan ##

  environment location: C:\Users\ai\miniconda3\envs\torch312

  added / updated specs:
    - python=3.12


The following packages will be downloaded:

    package                    |            build
    ---------------------------|-----------------
    ca-certificates-2025.9.9   |       haa95532_0         127 KB
    libzlib-1.3.1              |       h02ab6af_0          64 KB
    openssl-3.0.18             |       h543e019_0         6.8 MB
    pip-25.2                   |     pyhc872135_0         1.2 MB
    python-3.12.11             |       h716150d_0        16.5 MB
    setuptools-80.9.0          |  py312haa95532_0         1.8 MB
    wheel-0.45.1               |  py312haa95532_0         177 KB
    zlib-1.3.1                 |       h02ab6af_0         113 KB
    ------------------------------------------------------------
                                           Total:        26.9 MB

The following NEW packages will be INSTALLED:

  bzip2              pkgs/main/win-64::bzip2-1.0.8-h2bbff1b_6
  ca-certificates    pkgs/main/win-64::ca-certificates-2025.9.9-haa95532_0
  expat              pkgs/main/win-64::expat-2.7.1-h8ddb27b_0
  libffi             pkgs/main/win-64::libffi-3.4.4-hd77b12b_1
  libzlib            pkgs/main/win-64::libzlib-1.3.1-h02ab6af_0
  openssl            pkgs/main/win-64::openssl-3.0.18-h543e019_0
  pip                pkgs/main/noarch::pip-25.2-pyhc872135_0
  python             pkgs/main/win-64::python-3.12.11-h716150d_0
  setuptools         pkgs/main/win-64::setuptools-80.9.0-py312haa95532_0
  sqlite             pkgs/main/win-64::sqlite-3.50.2-hda9a48d_1
  tk                 pkgs/main/win-64::tk-8.6.15-hf199647_0
  tzdata             pkgs/main/noarch::tzdata-2025b-h04d1e81_0
  ucrt               pkgs/main/win-64::ucrt-10.0.22621.0-haa95532_0
  vc                 pkgs/main/win-64::vc-14.3-h2df5915_10
  vc14_runtime       pkgs/main/win-64::vc14_runtime-14.44.35208-h4927774_10
  vs2015_runtime     pkgs/main/win-64::vs2015_runtime-14.44.35208-ha6b5a95_10
  wheel              pkgs/main/win-64::wheel-0.45.1-py312haa95532_0
  xz                 pkgs/main/win-64::xz-5.6.4-h4754444_1
  zlib               pkgs/main/win-64::zlib-1.3.1-h02ab6af_0



Downloading and Extracting Packages:

Preparing transaction: done
Verifying transaction: done
Executing transaction: done
#
# To activate this environment, use
#
#     $ conda activate torch312
#
# To deactivate an active environment, use
#
#     $ conda deactivate



# Open “Anaconda Prompt (Miniconda3)” (not PowerShell).
:: 1) Create a clean env with Python 3.12
conda create -n torch312 python=3.12 -y

:: 2) Activate it
conda activate torch312

:: 3) Install PyTorch GPU build (CUDA 12.1) via conda
conda install pytorch torchvision torchaudio pytorch-cuda=12.1 -c pytorch -c nvidia -y

:: 4) Add this env to Jupyter
pip install ipykernel notebook
python -m ipykernel install --user --name=torch312 --display-name "Python 3.12 (torch312)"

:: 5) Launch Jupyter
jupyter notebook
