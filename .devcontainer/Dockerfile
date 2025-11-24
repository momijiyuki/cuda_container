FROM nvidia/cuda:12.9.1-runtime-ubuntu22.04

ARG USERNAME="devconuser"
ARG USERUID="1000"
ARG USERGID="1000"
ARG PYTHON_VERSION="3.9"

ARG DEBIAN_FRONTEND=noninteractive


ENV LANG=ja_JP.UTF-8 \
    LANGUAGE=ja_JP:ja \
    LC_ALL=ja_JP.UTF-8 \
    TZ=JST-9 \
    TERM=xterm \
    PS1='${debian_chroot:+($debian_chroot)}\[\033[01;32m\]\u\[\033[00m\]:\[\033[01;34m\]\w\[\033[00m\]$(__git_ps1 "(%s)")\$ '

RUN apt update && \
    apt install software-properties-common -y && \
    add-apt-repository ppa:deadsnakes/ppa -y

COPY user_registration.sh /tmp/install_lib/
COPY bin/ /tmp/install_lib/bin/
COPY requirements.txt /home/$USERNAME/

RUN apt-get update && \
    apt-get purge -y imagemagick imagemagick-6-common && \
    apt-get install -y --no-install-recommends \
    build-essential \
    git \
    vim \
    curl \
    tree \
    sudo \
    tzdata \
    sysstat \
    python${PYTHON_VERSION}-dev \
    python${PYTHON_VERSION}-tk \
    ca-certificates \
    openssh-client && \
    apt-get -y upgrade --no-install-recommends && \
    apt-get autoremove -y && \
    apt-get -y clean && \
    rm -rf /var/lib/apt/lists/* && \
    curl -kL https://bootstrap.pypa.io/get-pip.py | python${PYTHON_VERSION} && \
    bash /tmp/install_lib/user_registration.sh && \
    rm -r /tmp/install_lib/

# RUN pip install numpy torch matplotlib torchvision

WORKDIR /home/$USERNAME

RUN curl -o /home/$USERNAME/.git-completion.bash https://raw.githubusercontent.com/git/git/master/contrib/completion/git-completion.bash &&\
    curl -o /home/$USERNAME/.git-prompt.sh https://raw.githubusercontent.com/git/git/master/contrib/completion/git-prompt.sh && \
    pip install --no-cache-dir -r /home/$USERNAME/requirements.txt && \
    echo 'PATH="$HOME/.local/bin:$PATH"' >> /home/$USERNAME/.bashrc && \
    echo 'alias python="python'${PYTHON_VERSION}'"' >> /home/$USERNAME/.bashrc && \
    echo 'source ~/.git-completion.bash' >> /home/$USERNAME/.bashrc && \
    echo 'source ~/.git-prompt.sh\nGIT_PS1_SHOWDIRTYSTATE=true' >> /home/$USERNAME/.bashrc && \
    echo "PS1='"${PS1}"'" >> /home/$USERNAME/.bashrc

USER $USERNAME
