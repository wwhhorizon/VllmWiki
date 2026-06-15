# vllm-project/vllm#7813: [Bug]: Docker build for ROCm fails for latest release and main branch

| 字段 | 值 |
| --- | --- |
| Issue | [#7813](https://github.com/vllm-project/vllm/issues/7813) |
| 状态 | closed |
| 标签 | bug;rocm |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;frontend_api;hardware_porting |
| 子分类 | install |
| Operator 关键词 | cuda;triton |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Docker build for ROCm fails for latest release and main branch

### Issue 正文摘录

### Your current environment Server with MI300X GPUs ### 🐛 Describe the bug Build the vLLM ROCm image by following this [link](https://docs.vllm.ai/en/latest/getting_started/amd-installation.html) The Docker build fails with the following error: ``` > [build_triton 1/1] RUN --mount=type=cache,target=/root/.cache/ccache if [ "1" = "1" ]; then mkdir -p libs && cd libs && git clone https://github.com/OpenAI/triton.git && cd triton && git checkout "main" && cd python && python3 setup.py bdist_wheel --dist-dir=/install; else mkdir -p /install; fi: 0.241 Cloning into 'triton'... 10.80 Already on 'main' 10.80 Your branch is up to date with 'origin/main'. 140.4 downloading and extracting https://anaconda.org/nvidia/cuda-nvcc/12.4.99/download/linux-64/cuda-nvcc-12.4.99-0.tar.bz2 ... 140.4 Traceback (most recent call last): 140.4 File "/opt/conda/envs/py_3.9/lib/python3.9/urllib/request.py", line 1346, in do_open 140.4 h.request(req.get_method(), req.selector, req.data, headers, 140.4 File "/opt/conda/envs/py_3.9/lib/python3.9/http/client.py", line 1285, in request 140.4 self._send_request(method, url, body, headers, encode_chunked) 140.4 File "/opt/conda/envs/py_3.9/lib/python3.9/http/clie...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: [Bug]: Docker build for ROCm fails for latest release and main branch bug;rocm ### Your current environment Server with MI300X GPUs ### 🐛 Describe the bug Build the vLLM ROCm image by following this [link](https://docs....
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: [Bug]: Docker build for ROCm fails for latest release and main branch bug;rocm ### Your current environment Server with MI300X GPUs ### 🐛 Describe the bug Build the vLLM ROCm image by following this [link](https://docs....
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: n.html) The Docker build fails with the following error: ``` > [build_triton 1/1] RUN --mount=type=cache,target=/root/.cache/ccache if [ "1" = "1" ]; then mkdir -p libs && cd libs && git clone https://github.com/OpenAI/...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: cd python && python3 setup.py bdist_wheel --dist-dir=/install; else mkdir -p /install; fi: 0.241 Cloning into 'triton'... 10.80 Already on 'main' 10.80 Your branch is up to date with 'origin/main'. 140.4 downloading and...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: nt call last): 140.4 File "/opt/conda/envs/py_3.9/lib/python3.9/urllib/request.py", line 1346, in do_open 140.4 h.request(req.get_method(), req.selector, req.data, headers, 140.4 File "/opt/conda/envs/py_3.9/lib/python3...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
