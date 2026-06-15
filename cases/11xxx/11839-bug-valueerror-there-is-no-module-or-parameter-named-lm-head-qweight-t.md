# vllm-project/vllm#11839: [Bug]: ValueError: There is no module or parameter named 'lm_head.qweight_type' in Qwen2ForCausalLM.When use GGUF and draft model

| 字段 | 值 |
| --- | --- |
| Issue | [#11839](https://github.com/vllm-project/vllm/issues/11839) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: ValueError: There is no module or parameter named 'lm_head.qweight_type' in Qwen2ForCausalLM.When use GGUF and draft model

### Issue 正文摘录

### Your current environment ### Model Input Dumps ```output ValueError Traceback (most recent call last) Cell In[5], [line 6](vscode-notebook-cell:?execution_count=5&line=6) [3](vscode-notebook-cell:?execution_count=5&line=3) prompts = ["The future of AI is"] [4](vscode-notebook-cell:?execution_count=5&line=4) sampling_params = SamplingParams(temperature=0.8, top_p=0.95) ----> [6](vscode-notebook-cell:?execution_count=5&line=6) llm = LLM( [7](vscode-notebook-cell:?execution_count=5&line=7) model=MODLE_PATH, [8](vscode-notebook-cell:?execution_count=5&line=8) tensor_parallel_size=1, [9](vscode-notebook-cell:?execution_count=5&line=9) speculative_model=SPECULATIVE_MODLE_PATH, [10](vscode-notebook-cell:?execution_count=5&line=10) num_speculative_tokens=5, [11](vscode-notebook-cell:?execution_count=5&line=11) use_v2_block_manager=True, [12](vscode-notebook-cell:?execution_count=5&line=12) ) File ~/anaconda3/lib/python3.12/site-packages/vllm/utils.py:986, in deprecate_args. .wrapper. .inner(*args, **kwargs) [979](https://vscode-remote+wsl-002bubuntu-002d24-002e04.vscode-resource.vscode-cdn.net/mnt/d/my/work/study/ai/kaggle_code/aimo2/test/draft/~/anaconda3/lib/python3.12/site-packages...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: meter named 'lm_head.qweight_type' in Qwen2ForCausalLM.When use GGUF and draft model bug;stale ### Your current environment ### Model Input Dumps ```output ValueError Traceback (most recent call last) Cell In[5], [line...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: When use draft model in GGUF model.Then error. ```python from modelscope import snapshot_download from modelscope.hub.file_download import model_file_download # SPECULATIVE_MODLE_PATH = snapshot_download('PowerInfer/Sma...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: ueError: There is no module or parameter named 'lm_head.qweight_type' in Qwen2ForCausalLM.When use GGUF and draft model bug;stale ### Your current environment ### Model Input Dumps ```output ValueError Traceback (most r...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: l_file_download # SPECULATIVE_MODLE_PATH = snapshot_download('PowerInfer/SmallThinker-3B-Preview') SPECULATIVE_MODLE_PATH = model_file_download(model_id='bartowski/SmallThinker-3B-Preview-GGUF',file_path='SmallThinker-3...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: init, trust_remote_code, allowed_local_media_path, tensor_parallel_size, dtype, quantization, revision, tokenizer_revision, seed, gpu_memory_utilization, swap_space, cpu_offload_gb, enforce_eager, max_seq_len_to_capture...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
