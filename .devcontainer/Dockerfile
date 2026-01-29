FROM mcr.microsoft.com/devcontainers/python:3.12-bookworm

# Remove the Yarn repository with the expired GPG key to prevent apt-get update failures
RUN rm -f /etc/apt/sources.list.d/yarn.list 2>/dev/null || true
