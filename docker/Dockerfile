FROM ubuntu:20.04

ENV DEBCONF_NOWARNINGS=yes

ENV NVIDIA_VISIBLE_DEVICES ${NVIDIA_VISIBLE_DEVICES:-all}
ENV NVIDIA_DRIVER_CAPABILITIES ${NVIDIA_DRIVER_CAPABILITIES:+$NVIDIA_DRIVER_CAPABILITIES,}graphics

# rosのインストール時にtzdataのタイムゾーン選択で止まらないように
ENV DEBIAN_FRONTEND=noninteractive
# aptを日本のミラーに設定  http://www.aise.ics.saitama-u.ac.jp/~gotoh/HowToInstallUbuntu1804OnWSL.html
RUN sed -i.bak -e "s/http:\/\/archive\.ubuntu\.com/http:\/\/jp\.archive\.ubuntu\.com/g" /etc/apt/sources.list

# コンテナにプロキシの環境変数を追加する
ENV https_proxy "http://wwwproxy.kanazawa-it.ac.jp:8080"
ENV http_proxy "http://wwwproxy.kanazawa-it.ac.jp:8080"

RUN apt-get update
# sudo:sudo x11-apps:xeyes用 net-tools:ifconfig用 mesa-utils:glxgears用 gnupg:rosのadd-key用
RUN apt-get install -y sudo gnupg x11-apps iputils-ping net-tools mesa-utils vim-gtk emacs dbus-x11 terminator git

# ROSのインストール
RUN apt-get update
RUN apt-get install -y curl gnupg2 lsb-release
RUN curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key -o /usr/share/keyrings/ros-archive-keyring.gpg
RUN echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu $(lsb_release -cs) main" | tee /etc/apt/sources.list.d/ros2.list > /dev/null
RUN apt-get -y update
RUN apt-get install -y ros-foxy-desktop
RUN echo "source /opt/ros/foxy/setup.bash" >> ~/.bashrc
RUN apt-get install -y python3-argcomplete python3-pip
RUN apt-get install -y python3-colcon-common-extensions

# 使いたいパッケージのインストール
# RUN apt-get -y install (ここに使いたいパッケージを列挙する)
# open manipulator x =============================
RUN apt -y install ros-foxy-vision-opencv
RUN apt -y install python3-pip
RUN pip3 install scipy
RUN pip3 install opencv-contrib-python==4.6.0.66 transforms3d
RUN apt -y install ros-foxy-turtle-tf2-py ros-foxy-tf2-tools ros-foxy-tf-transformations
RUN apt -y install ros-foxy-usb-cam
# ================================================


# aptのキャッシュを削除してイメージの容量削減
RUN rm -rf /var/lib/apt/lists/
