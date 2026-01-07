if ! grep -qi 'kernel.core_pattern' /etc/sysctl.conf; then
  sudo sh -c 'echo "kernel.core_pattern=core.%p.%u.%s.%e.%t" >> /etc/sysctl.conf'
  sudo sysctl -p
fi
ulimit -c unlimited
