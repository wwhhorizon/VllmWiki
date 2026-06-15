# vllm-project/vllm#12826: [Bug]: [V1] Mamba models fail on profile run

| 字段 | 值 |
| --- | --- |
| Issue | [#12826](https://github.com/vllm-project/vllm/issues/12826) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits |
| 子分类 |  |
| Operator 关键词 | cuda;sampling;triton |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: [V1] Mamba models fail on profile run

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Running Mamba models using the v1 engine fails due to an error in the `MambaCacheManager` during the profile run. ``` from vllm import LLM, SamplingParams import os os.environ["VLLM_USE_V1"] = "1" prompts = [ "Hello, my name is", "The president of the United States is", "The capital of France is", "The future of AI is", ] sampling_params = SamplingParams(temperature=0.8, top_p=0.95) #llm = LLM(model="ai21labs/Jamba-tiny-dev", enable_prefix_caching=False) llm = LLM(model="state-spaces/mamba-130m-hf", enable_prefix_caching=False) outputs = llm.generate(prompts, sampling_params) # Print the outputs. for output in outputs: prompt = output.prompt generated_text = output.outputs[0].text print(f"Prompt: {prompt!r}, Generated text: {generated_text!r}") ``` ``` ERROR 02-06 12:00:04 core.py:208] EngineCore hit an exception: Traceback (most recent call last): ERROR 02-06 12:00:04 core.py:208] File "/scratch/micromamba/envs/vllm-0.7.1/lib/python3.12/site-packages/vllm/v1/engine/core.py", line 200, in run_engine_core ERROR 02-06 12:00:04 core.py:208] engine_core = EngineCoreProc(*args, **kwargs) ERROR 02-06 12:00:04 core.py:208] ^^^^^^^^^^^^^...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: error in the `MambaCacheManager` during the profile run. ``` from vllm import LLM, SamplingParams import os os.environ["VLLM_USE_V1"] = "1" prompts = [ "Hello, my name is", "The president of the United States is", "The...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: 95) #llm = LLM(model="ai21labs/Jamba-tiny-dev", enable_prefix_caching=False) llm = LLM(model="state-spaces/mamba-130m-hf", enable_prefix_caching=False) outputs = llm.generate(prompts, sampling_params) # Print the output...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: [V1] Mamba models fail on profile run bug;stale ### Your current environment ### 🐛 Describe the bug Running Mamba models using the v1 engine fails due to an error in the `MambaCacheManager` during the profile run...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: [V1] Mamba models fail on profile run bug;stale ### Your current environment ### 🐛 Describe the bug Running Mamba models using the v1 engine fails due to an error in the `MambaCacheManager` during the profile run...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
