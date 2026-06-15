# vllm-project/vllm#7953: [Bug]: Can't find safetensors model weights

| 字段 | 值 |
| --- | --- |
| Issue | [#7953](https://github.com/vllm-project/vllm/issues/7953) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Can't find safetensors model weights

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When loading a model with weights in safetensors format, no files are found despite being there which causes an error. Example code: ```python llm = LLM(model="TinyLlama/TinyLlama-1.1B-Chat-v1.0", load_format="safetensors") ``` Error: ```RuntimeError: Cannot find any model weights with...``` I located the problem to the method ```_prepare_weights``` in ```vllm/vllm/model_executor/model_loader/loader.py``` in this section: ```python if use_safetensors: # For models like Mistral-7B-Instruct-v0.3 # there are both sharded safetensors files and a consolidated # safetensors file. Using both breaks. # Here, we download the `model.safetensors.index.json` and filter # any files not found in the index. if not is_local: download_safetensors_index_file_from_hf( model_name_or_path, self.load_config.download_dir, revision) hf_weights_files = filter_duplicate_safetensors_files( hf_weights_files, hf_folder) else: hf_weights_files = filter_files_not_needed_for_inference( hf_weights_files) if len(hf_weights_files) == 0: raise RuntimeError( f"Cannot find any model weights with `{model_name_or_path}`") ``` I checked the length of ```hf_weight_files`...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: Can't find safetensors model weights bug;stale ### Your current environment ### 🐛 Describe the bug When loading a model with weights in safetensors format, no files are found despite being there which causes an e...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_in...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: r_duplicate_safetensors_files( hf_weights_files, hf_folder) else: hf_weights_files = filter_files_not_needed_for_inference( hf_weights_files) if len(hf_weights_files) == 0: raise RuntimeError( f"Cannot find any model we...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ed. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: Can't find safetensors model weights bug;stale ### Your current environment ### 🐛 Describe the bug When loading a model with weights in safetensors format, no files are found despite being there which causes an e...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
