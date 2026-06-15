# vllm-project/vllm#21180: [Bug]: Dockerfile consolidation

| 字段 | 值 |
| --- | --- |
| Issue | [#21180](https://github.com/vllm-project/vllm/issues/21180) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Dockerfile consolidation

### Issue 正文摘录

### Your current environment Any platform that can run containers. ### 🐛 Describe the bug These Dockerfiles should be consolidated, there's lots of inconsistencies that are causing issues: https://github.com/vllm-project/vllm/tree/main/docker An example of what is essentially Dockerfile.cpu and Dockerfile.arm consolidated (buildable on both arches) is: ``` FROM ubuntu:24.04 AS base WORKDIR /workspace/ ENV PATH="/root/.local/bin:$PATH" ENV VIRTUAL_ENV="/opt/venv" ENV UV_PYTHON_INSTALL_DIR="/opt/uv/python" ENV PATH="$VIRTUAL_ENV/bin:$PATH" ENV UV_HTTP_TIMEOUT=500 ENV UV_INDEX_STRATEGY="unsafe-best-match" ENV UV_LINK_MODE="copy" RUN /dev/null } main() { set -eux -o pipefail if available dnf; then dnf install -y git curl wget ca-certificates gcc gcc-c++ \ gperftools-libs numactl-devel ffmpeg libSM libXext mesa-libGL jq lsof \ vim numactl dnf -y clean all rm -rf /var/cache/*dnf* elif available apt-get; then apt-get update -y apt-get install -y --no-install-recommends git curl wget ca-certificates \ gcc g++ libtcmalloc-minimal4 libnuma-dev ffmpeg libsm6 libxext6 libgl1 \ jq lsof vim numactl rm -rf /var/lib/apt/lists/* fi curl -LsSf https://astral.sh/uv/0.7.21/install.sh | bash } main "$...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: [Bug]: Dockerfile consolidation bug;stale ### Your current environment Any platform that can run containers. ### 🐛 Describe the bug These Dockerfiles should be consolidated, there's lots of inconsistencies that are caus...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: tially Dockerfile.cpu and Dockerfile.arm consolidated (buildable on both arches) is: ``` FROM ubuntu:24.04 AS base WORKDIR /workspace/ ENV PATH="/root/.local/bin:$PATH" ENV VIRTUAL_ENV="/opt/venv" ENV UV_PYTHON_INSTALL_...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: ]; then export VLLM_CPU_DISABLE_AVX512="0" export VLLM_CPU_AVX512BF16="0" export VLLM_CPU_AVX512VNNI="0" elif [ "$arch" == "aarch64" ]; then export VLLM_CPU_DISABLE_AVX512="true" fi pip_install requirements/cpu-build.tx...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: Dockerfile consolidation bug;stale ### Your current environment Any platform that can run containers. ### 🐛 Describe the bug These Dockerfiles should be consolidated, there's lots of inconsistencies that are caus...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
