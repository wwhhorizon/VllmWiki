# vllm-project/vllm#15539: [Bug]: Error when inference on llava-1.6-34B

| 字段 | 值 |
| --- | --- |
| Issue | [#15539](https://github.com/vllm-project/vllm/issues/15539) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;multimodal_vlm;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Error when inference on llava-1.6-34B

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When using llava-1/6-34b for inference, I found the follow warning and error when processing the inputs: WARNING 03-26 17:43:58 utils.py:432] **The number of multi-modal placeholder tokens in the prompt is less than the number of multi-modal inputs. Extra placeholder tokens will be treated as plain text** [rank0]: **ValueError: Multi-modal placeholders and items must have the same length.** Processed prompts: 0%| | 0/4139 [00:00 \n{}\nASSISTANT:" # model_type = args.model_type model_path = model_path_map["llava"][model_name] llm = LLM(model=model_path, gpu_memory_utilization=0.9) stop_token_ids = None return llm, prompt_template, stop_token_ids model_example_map = { "llava": run_llava, # "llava-next": run_llava_next, # "phi3_v": run_phi3v, # "chameleon": run_chameleon, # "minicpmv": run_minicpmv, # "blip-2": run_blip2, # "internvl_chat": run_internvl, # "qwen_vl": run_qwen_vl, } sampling_params = SamplingParams( temperature=0.0, max_tokens=8, stop_token_ids=stop_token_ids, ) inputs.append({ "prompt": prompt_template.format(question), "multi_modal_data": { "image": image }, }) answers.append(data_instance["answer"]) outputs = llm....

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: | 0/4139 [00:00 \n{}\nASSISTANT:" # model_type = args.model_type model_path = model_path_map["llava"][model_name] llm = LLM(model=model_path, gpu_memory_utilization=0.9) stop_token_ids = None return llm, prompt_template...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;hardware_porting;model_support;multimodal_vlm;sampling_logits;speculative_decoding cuda;operator;sampling;triton bui...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: 34B ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ltimodal_vlm;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_dependency;memory_layout Your current environment
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: cuda;operator;sampling;triton build_error;nan_inf env_dependency;memory_layout Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
