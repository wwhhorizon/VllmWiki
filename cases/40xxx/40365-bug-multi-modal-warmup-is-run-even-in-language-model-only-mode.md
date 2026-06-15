# vllm-project/vllm#40365: [Bug]: Multi-modal warmup is run even in `language_model_only` mode

| 字段 | 值 |
| --- | --- |
| Issue | [#40365](https://github.com/vllm-project/vllm/issues/40365) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;multimodal_vlm;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;gemm;operator;sampling;triton |
| 症状 | build_error;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Multi-modal warmup is run even in `language_model_only` mode

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When hosting multi-modal models (such as Gemma 4), there is no way to disable the multimodal warmup that happens, which extends the cold start time of vLLM unnecessarily. As we are running vLLM in a latency-sensitive autoscaling environment it would be great to avoid this. Even when specifying `--limit-mm-per-prompt '{"image": 0, "video": 0, "audio": 0}'` and `--language_model_only` as per the documentation, we see in the output: ``` (APIServer pid=3) INFO 04-20 13:30:52 [registry.py:126] All limits of multimodal modalities supported by the model are set to 0, running in text-only mode ... (APIServer pid=3) INFO 04-20 13:28:46 [hf.py:314] Detected the chat template content format to be 'openai'. You can set `--chat-template-content-format` to override this. (APIServer pid=3) INFO 04-20 13:28:57 [base.py:245] Multi-modal warmup completed in 10.868s ``` ### To reproduce ``` vllm serve RedHatAI/gemma-4-31B-it-FP8-block \ --language-model-only \ --limit-mm-per-prompt '{"image": 0, "video": 0, "audio": 0}' \ --max-model-len 8192 --max-num-seqs 4 ``` and see logs. ### Likely root cause [`BaseRenderer.warmup()`](https://github.com/vllm-...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 7: [Bug]: Multi-modal warmup is run even in `language_model_only` mode bug ### Your current environment ### 🐛 Describe the bug When hosting multi-modal models (such as Gemma 4), there is no way to disable the multimodal wa...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: e autoscaling environment it would be great to avoid this. Even when specifying `--limit-mm-per-prompt '{"image": 0, "video": 0, "audio": 0}'` and `--language_model_only` as per the documentation, we see in the output:...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: n 10.868s ``` ### To reproduce ``` vllm serve RedHatAI/gemma-4-31B-it-FP8-block \ --language-model-only \ --limit-mm-per-prompt '{"image": 0, "video": 0, "audio": 0}' \ --max-model-len 8192 --max-num-seqs 4 ``` and see...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: , so the HF processor is run on a dummy image (plus video/audio if the arch supports them) regardless of the user's zero limits. ### Possible fix One-line change at [`vllm/renderers/base.py:223`](https://github.com/vllm...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: .868s ``` ### To reproduce ``` vllm serve RedHatAI/gemma-4-31B-it-FP8-block \ --language-model-only \ --limit-mm-per-prompt '{"image": 0, "video": 0, "audio": 0}' \ --max-model-len 8192 --max-num-seqs 4 ``` and see logs...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
