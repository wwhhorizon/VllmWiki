# vllm-project/vllm#24297: [Bug]: Crash on --otlp-traces-endpoint=${OTEL_EXPORTER_OTLP_TRACES_ENDPOINT} when CPU mode

| 字段 | 值 |
| --- | --- |
| Issue | [#24297](https://github.com/vllm-project/vllm/issues/24297) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Crash on --otlp-traces-endpoint=${OTEL_EXPORTER_OTLP_TRACES_ENDPOINT} when CPU mode

### Issue 正文摘录

### Your current environment I have a Dockerfile I need to maintain because this project both doesn't publish one and also requires manual installation of otel libs ```Dockerfile # Pytorch doesn't build on Alpine, so we use Ubuntu instead. # We can't use the official Pytorch image because it is x86 only. FROM ubuntu:24.04 ARG VLLM_VERSION=v0.10.1.1 # Package pre-reqs copied from https://github.com/vllm-project/vllm/blob/main/docker/Dockerfile.arm ENV CCACHE_DIR=/root/.cache/ccache ENV CMAKE_CXX_COMPILER_LAUNCHER=ccache RUN --mount=type=cache,target=/var/cache/apt \ apt-get update -y \ && apt-get install -y curl ccache git wget vim numactl gcc-12 g++-12 python3 python3-pip libtcmalloc-minimal4 libnuma-dev \ && apt-get install -y ffmpeg libsm6 libxext6 libgl1 \ && update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-12 10 --slave /usr/bin/g++ g++ /usr/bin/g++-12 # Install CMake 3.26+, required for installation RUN --mount=type=cache,target=/var/cache/apt \ wget -O - https://apt.kitware.com/keys/kitware-archive-latest.asc 2>/dev/null | gpg --dearmor - | tee /usr/share/keyrings/kitware-archive-keyring.gpg >/dev/null \ && . /etc/os-release \ && echo "deb [signed-by=/usr/share/ke...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 9: ENDPOINT} when CPU mode bug;stale ### Your current environment I have a Dockerfile I need to maintain because this project both doesn't publish one and also requires manual installation of otel libs ```Dockerfile # Pyto...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: Resolved architecture: Qwen3ForCausalLM vllm | (APIServer pid=7) `torch_dtype` is deprecated! Use `dtype` instead! vllm | (APIServer pid=7) INFO 09-05 06:01:00 [__init__.py:1750] Using max model len 4096 vllm | (APIServ...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: org/whl/cpu RUN VLLM_TARGET_DEVICE=cpu python setup.py install ENV CHAT_MODEL=Qwen/Qwen3-0.6B ENV OTEL_EXPORTER_OTLP_TRACES_ENDPOINT=http://localhost:11434/v1/traces EXPOSE 8000 CMD vllm serve ${CHAT_MODEL} --max-num-ba...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: -traces-endpoint=${OTEL_EXPORTER_OTLP_TRACES_ENDPOINT} when CPU mode bug;stale ### Your current environment I have a Dockerfile I need to maintain because this project both doesn't publish one and also requires manual i...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: (EngineCore_0 pid=55) INFO 09-05 05:58:17 [cpu.py:100] Using Torch SDPA backend. vllm | (EngineCore_0 pid=55) INFO 09-05 05:58:18 [weight_utils.py:296] Using model weights format ['*.safetensors'] ``` If I add --otlp-tr...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
