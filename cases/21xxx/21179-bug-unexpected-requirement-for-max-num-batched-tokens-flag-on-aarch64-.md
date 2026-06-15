# vllm-project/vllm#21179: [Bug]: Unexpected requirement for --max-num-batched-tokens flag on aarch64 Linux VMs (macbooks)

| 字段 | 值 |
| --- | --- |
| Issue | [#21179](https://github.com/vllm-project/vllm/issues/21179) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Unexpected requirement for --max-num-batched-tokens flag on aarch64 Linux VMs (macbooks)

### Issue 正文摘录

### Your current environment docker/podman on macOS aarch64 and docker/podman on Fedora 42 x86_64 using this Dockerfile: ``` FROM ubuntu:24.04 AS base WORKDIR /workspace/ ENV PATH="/root/.local/bin:$PATH" ENV VIRTUAL_ENV="/opt/venv" ENV UV_PYTHON_INSTALL_DIR="/opt/uv/python" ENV PATH="$VIRTUAL_ENV/bin:$PATH" ENV UV_HTTP_TIMEOUT=500 ENV UV_INDEX_STRATEGY="unsafe-best-match" ENV UV_LINK_MODE="copy" RUN /dev/null } main() { set -eux -o pipefail if available dnf; then dnf install -y git curl wget ca-certificates gcc gcc-c++ \ gperftools-libs numactl-devel ffmpeg libSM libXext mesa-libGL jq lsof \ vim numactl dnf -y clean all rm -rf /var/cache/*dnf* elif available apt-get; then apt-get update -y apt-get install -y --no-install-recommends git curl wget ca-certificates \ gcc g++ libtcmalloc-minimal4 libnuma-dev ffmpeg libsm6 libxext6 libgl1 \ jq lsof vim numactl rm -rf /var/lib/apt/lists/* fi curl -LsSf https://astral.sh/uv/0.7.21/install.sh | bash } main "$@" EOF RUN > /etc/environment fi echo 'ulimit -c 0' >> ~/.bashrc } pip_install() { local url="https://download.pytorch.org/whl/cpu" uv pip install -v -r "$1" --extra-index-url $url } git_clone_specific_commit() { local repo="${vllm_ur...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: on aarch64 Linux VMs (macbooks) bug;stale ### Your current environment docker/podman on macOS aarch64 and docker/podman on Fedora 42 x86_64 using this Dockerfile: ``` FROM ubuntu:24.04 AS base WORKDIR /workspace/ ENV PA...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: tokens 8192` when running: ``` vllm serve --max-num-batched-tokens 8192 HuggingFaceTB/SmolLM2-135M-Instruct ``` If this flag is not set, you get the following error: ``` Value error, max_num_batched_tokens (2048) is sma...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Bug]: Unexpected requirement for --max-num-batched-tokens flag on aarch64 Linux VMs (macbooks) bug;stale ### Your current environment docker/podman on macOS aarch64 and docker/podman on Fedora 42 x86_64 using this Dock...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: ]; then export VLLM_CPU_DISABLE_AVX512="0" export VLLM_CPU_AVX512BF16="0" export VLLM_CPU_AVX512VNNI="0" elif [ "$arch" == "aarch64" ]; then export VLLM_CPU_DISABLE_AVX512="true" fi pip_install requirements/cpu-build.tx...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: =value_error, input_value=ArgsKwargs((), {'runner_t...ync_scheduling': False}), input_type=ArgsKwargs] ``` This was not required previously for aarch64, and is not required for x86_64 when running identical commands. It...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
