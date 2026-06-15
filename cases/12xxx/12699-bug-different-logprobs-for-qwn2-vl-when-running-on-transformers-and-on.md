# vllm-project/vllm#12699: [Bug]: different logprobs for qwn2-vl when running on transformers and on vllm

| 字段 | 值 |
| --- | --- |
| Issue | [#12699](https://github.com/vllm-project/vllm/issues/12699) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 30; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: different logprobs for qwn2-vl when running on transformers and on vllm

### Issue 正文摘录

### Your current environment Im runnig a finetuned qwen2-vl with transformers and with vllm and getting significantly different logprobs. vllm is running on runpod vllm-worker and the environment data is in the attached file: [pod_env.txt](https://github.com/user-attachments/files/18644453/pod_env.txt) tranformers env data: Package Version --------------------------------- --------------- accelerate 0.34.0 annotated-types 0.7.0 anyio 4.2.0 argon2-cffi 23.1.0 argon2-cffi-bindings 21.2.0 arrow 1.3.0 asttokens 2.4.1 async-lru 2.0.4 attrs 23.2.0 av 14.1.0 Babel 2.14.0 beautifulsoup4 4.12.3 bleach 6.1.0 blinker 1.4 certifi 2024.2.2 cffi 1.16.0 charset-normalizer 3.3.2 click 8.1.8 comm 0.2.1 cryptography 3.4.8 dbus-python 1.2.18 debugpy 1.8.0 decorator 5.1.1 defusedxml 0.7.1 distro 1.7.0 docker-pycreds 0.4.0 einops 0.8.0 entrypoints 0.4 exceptiongroup 1.2.0 executing 2.0.1 fastjsonschema 2.19.1 filelock 3.13.1 flash-attn 2.7.2.post1 fqdn 1.5.1 fsspec 2024.2.0 gitdb 4.0.12 GitPython 3.1.44 h11 0.14.0 httpcore 1.0.2 httplib2 0.20.2 httpx 0.26.0 huggingface-hub 0.27.1 idna 3.6 importlib-metadata 4.6.4 ipykernel 6.29.0 ipython 8.21.0 ipython-genutils 0.2.0 ipywidgets 8.1.1 isoduration 20.11...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: 453/pod_env.txt) tranformers env data: Package Version --------------------------------- --------------- accelerate 0.34.0 annotated-types 0.7.0 anyio 4.2.0 argon2-cffi 23.1.0
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: nd on vllm bug;stale ### Your current environment Im runnig a finetuned qwen2-vl with transformers and with vllm and getting significantly different logprobs. vllm is running on runpod vllm-worker and the environment da...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: 4.21.1 jsonschema-specifications 2023.12.1 jupyter-archive 3.4.0 jupyter_client 7.4.9 jupyter_contrib_core 0.4.2 jupyter_contrib_nbextensions 0.7.0 jupyter_core 5.7.1 jupyter-events
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: 0.27.1 idna 3.6 importlib-metadata 4.6.4 ipykernel 6.29.0 ipython 8.21.0 ipython-genutils 0.2.0 ipywidgets 8.1.1 isoduration
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ferent logprobs for qwn2-vl when running on transformers and on vllm bug;stale ### Your current environment Im runnig a finetuned qwen2-vl with transformers and with vllm and getting significantly different logprobs. vl...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
