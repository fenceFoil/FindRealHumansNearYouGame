# Reset Git, Pull updates, build app dist, and start everything
git clean -fd && git pull && ./build_app_dist.sh && ./run_all.sh