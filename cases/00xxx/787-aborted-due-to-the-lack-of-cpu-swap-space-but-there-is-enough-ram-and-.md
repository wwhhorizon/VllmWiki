# vllm-project/vllm#787: Aborted due to the lack of CPU swap space, but there is enough RAM and swap

| 字段 | 值 |
| --- | --- |
| Issue | [#787](https://github.com/vllm-project/vllm/issues/787) |
| 状态 | closed |
| 标签 |  |
| 评论 | 14; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | model_support;sampling_logits;scheduler_memory |
| 子分类 |  |
| Operator 关键词 | cuda;sampling |
| 症状 |  |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> Aborted due to the lack of CPU swap space, but there is enough RAM and swap

### Issue 正文摘录

Ubuntu 22.04 (up to date, recently installed) nVidia 4090 CUDA 11.8 cuDNN 8.9.4.25 vLLM compiled from source: `d1744376` Model: `ehartford/dolphin-llama2-7b` ```python llm = LLM(model=model_path, dtype='bfloat16') sampling_params = SamplingParams(n=50, max_tokens=600, temperature=0.2, top_p=0.95) results = llm.generate(prompts, sampling_params, use_tqdm=True) ``` 200 prompts were prepared according to the model card's prompt template. The point of failure seems to be random. There is enough memory and swap. I don't know why it even requires any swap... ``` $ free -h total used free shared buff/cache available Mem: 62Gi 5,8Gi 13Gi 45Mi 43Gi 56Gi Swap: 31Gi 787Mi 31Gi ``` Nor the memory, not the swap use spikes/changes at all when the failure happens. Monitored it with 1s period. Full exception: ``` ... File "/home/viktor/ts/venv/lib/python3.10/site-packages/vllm-0.1.3-py3.10-linux-x86_64.egg/vllm/entrypoints/llm.py", line 130, in generate File "/home/viktor/ts/venv/lib/python3.10/site-packages/vllm-0.1.3-py3.10-linux-x86_64.egg/vllm/entrypoints/llm.py", line 150, in _run_engine File "/home/viktor/ts/venv/lib/python3.10/site-packages/vllm-0.1.3-py3.10-linux-x86_64.egg/vllm/engine/ll...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: ace, but there is enough RAM and swap Ubuntu 22.04 (up to date, recently installed) nVidia 4090 CUDA 11.8 cuDNN 8.9.4.25 vLLM compiled from source: `d1744376` Model: `ehartford/dolphin-llama2-7b` ```python llm = LLM(mod...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: el: `ehartford/dolphin-llama2-7b` ```python llm = LLM(model=model_path, dtype='bfloat16') sampling_params = SamplingParams(n=50, max_tokens=600, temperature=0.2, top_p=0.95) results = llm.generate(prompts, sampling_para...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ia 4090 CUDA 11.8 cuDNN 8.9.4.25 vLLM compiled from source: `d1744376` Model: `ehartford/dolphin-llama2-7b` ```python llm = LLM(model=model_path, dtype='bfloat16') sampling_params = SamplingParams(n=50, max_tokens=600,...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: h RAM and swap Ubuntu 22.04 (up to date, recently installed) nVidia 4090 CUDA 11.8 cuDNN 8.9.4.25 vLLM compiled from source: `d1744376` Model: `ehartford/dolphin-llama2-7b` ```python llm = LLM(model=model_path, dtype='b...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ib/python3.10/site-packages/vllm-0.1.3-py3.10-linux-x86_64.egg/vllm/core/scheduler.py", line 251, in schedule File "/home/viktor/ts/venv/lib/python3.10/site-packages/vllm-0.1.3-py3.10-linux-x86_64.egg/vllm/core/schedule...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
