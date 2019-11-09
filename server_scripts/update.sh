# Reset Git, Pull updates, build app dist, and start everything
git clean -fd && git pull && ./build_app_dist.sh

echo "If you wish to restart the server re-run run_all.sh"