# vllm-project/vllm#1065: IGNORE - AWQ model does not generate any tokens

| 字段 | 值 |
| --- | --- |
| Issue | [#1065](https://github.com/vllm-project/vllm/issues/1065) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;model_support;quantization;sampling_logits |
| 子分类 | precision |
| Operator 关键词 | cuda;quantization;sampling |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> IGNORE - AWQ model does not generate any tokens

### Issue 正文摘录

Branch: **main `e3e79e9`** OS: **Ubuntu 22.04** CUDA: **11.8** PyTorch: **2.0.1+cu117** GPU: **2x 4090** Built vLLM from source according to [the instructions](https://vllm.readthedocs.io/en/latest/getting_started/installation.html#build-from-source). Model: [casperhansen/vicuna-7b-v1.5-awq](https://huggingface.co/casperhansen/vicuna-7b-v1.5-awq) Server startup command: ```sh python -O -u -m vllm.entrypoints.api_server \ --host=0.0.0.0 \ --port=7777 \ --model=$HOME/models/vicuna-7b-v1.5-awq \ --quantization=awq ``` The vLLM server happily starts and loads the model, serves the API requests, but does not generate any tokens. Prompt: ``` Below is an instruction that describes a task. Write a response that appropriately completes the request. USER: What are ways to earn more money with less work? ASSISTANT: ``` The server generates no tokens: ``` INFO 09-17 01:57:33 async_llm_engine.py:338] Received request ccdeee0ce4a44b4c8043f148a4e7ee37: prompt: 'Below is an instruction that describes a task. Write a response that appropriately completes the request.\n\nUSER: What are ways to earn more money with less work?\nASSISTANT:', sampling params: SamplingParams(n=1, best_of=1, presence_pen...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: [the instructions](https://vllm.readthedocs.io/en/latest/getting_started/installation.html#build-from-source). Model: [casperhansen/vicuna-7b-v1.5-awq](https://huggingface.co/casperhansen/vicuna-7b-v1.5-awq) Server star...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: not generate any tokens Branch: **main `e3e79e9`** OS: **Ubuntu 22.04** CUDA: **11.8** PyTorch: **2.0.1+cu117** GPU: **2x 4090** Built vLLM from source according to [the instructions](https://vllm.readthedocs.io/en/late...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: IGNORE - AWQ model does not generate any tokens Branch: **main `e3e79e9`** OS: **Ubuntu 22.04** CUDA: **11.8** PyTorch: **2.0.1+cu117** GPU: **2x 4090** Built vLLM from source according to [the instructions](https://vll...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: rked fine with the WizardCoder 13B model hosted by vLLM at full (16 bit) precision on two GPUs (`--tp 2`) and using the WIZARDCODER prompt. correctness ci_build;distributed_parallel;frontend_api;model_support;quantizati...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: \ --port=7777 \ --model=$HOME/models/vicuna-7b-v1.5-awq \ --quantization=awq ``` The vLLM server happily starts and loads the model, serves the API requests, but does not generate any tokens. Prompt: ``` Below is an ins...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
