# vllm-project/vllm#12929: [Bug]: V1 engine fails with offline batched inference code in V0 engine

| 字段 | 值 |
| --- | --- |
| Issue | [#12929](https://github.com/vllm-project/vllm/issues/12929) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 12; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits |
| 子分类 |  |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error;crash |
| 根因提示 | env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: V1 engine fails with offline batched inference code in V0 engine

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I'm inferencing multiple prompts (inconsistent length) with local vllm in python code. If changed to VLLM V1 engine, it fails. If reversed to V0 engine, it can finish without any error. The startup code is simplified like this: ```python model_path = "/nfs/llm_models/DeepSeek-R1-Distill-Qwen-32B" stop_token_ids = [151645, 151643] llm = LLM(model=model_path, tokenizer=None, tensor_parallel_size=torch.cuda.device_count(), trust_remote_code=True, gpu_memory_utilization=0.8) tokenizer = AutoTokenizer.from_pretrained(model_path) input_texts = [] for one_prompt in prompts: messages = [ {"role": "system", "content": ""}, {"role": "user", "content": one_prompt} ] text = tokenizer.apply_chat_template( messages, tokenize=False, add_generation_prompt=True ) input_texts.append(text) output_strs = llm.generate(input_texts, sampling_params, use_tqdm=True) ``` Here's the log and traceback: ``` Processed prompts: 0%| | 4/3549 [00:50<9:04:40, 9.22s/it, est. speed input: 48.56 toks/s, output: 12.39 toks/s](VllmWorker rank=0 pid=9923) ERROR 02-08 09:31:59 multiproc_executor.py:374] WorkerProc hit an exception: %s (VllmWorker rank=0 pid=9923) ERROR...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: tale ### Your current environment ### 🐛 Describe the bug I'm inferencing multiple prompts (inconsistent length) with local vllm in python code. If changed to VLLM V1 engine, it fails. If reversed to V0 engine, it can fi...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ] llm = LLM(model=model_path, tokenizer=None, tensor_parallel_size=torch.cuda.device_count(), trust_remote_code=True, gpu_memory_utilization=0.8) tokenizer = AutoTokenizer.from_pretrained(model_path) input_texts = [] fo...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: xt = tokenizer.apply_chat_template( messages, tokenize=False, add_generation_prompt=True ) input_texts.append(text) output_strs = llm.generate(input_texts, sampling_params, use_tqdm=True) ``` Here's the log and tracebac...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: h without any error. The startup code is simplified like this: ```python model_path = "/nfs/llm_models/DeepSeek-R1-Distill-Qwen-32B" stop_token_ids = [151645, 151643] llm = LLM(model=model_path, tokenizer=None, tensor_p...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: g]: V1 engine fails with offline batched inference code in V0 engine bug;stale ### Your current environment ### 🐛 Describe the bug I'm inferencing multiple prompts (inconsistent length) with local vllm in python code. I...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
