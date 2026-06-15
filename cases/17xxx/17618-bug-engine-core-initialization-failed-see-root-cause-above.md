# vllm-project/vllm#17618: [Bug]: Engine Core initialization failed. See root cause above

| 字段 | 值 |
| --- | --- |
| Issue | [#17618](https://github.com/vllm-project/vllm/issues/17618) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 45; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | frontend_api;model_support;sampling_logits |
| 子分类 | runtime_err |
| Operator 关键词 | cuda |
| 症状 | crash |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Engine Core initialization failed. See root cause above

### Issue 正文摘录

### Your current environment Colab notebooks, A100 ### 🐛 Describe the bug I have no idea what's wrong. This model works with normal pipeline, but fails with vllm. It was saved to 16 bit and built off Unsloth/Llama3.18b Instruct This works -> from transformers import pipeline prompt = ( "Do aliens suffer?" ) gen = pipeline("text-generation", model=best_model, tokenizer=tokenizer) print(gen(prompt, max_new_tokens=256, do_sample=True, temperature=0.7)[0]["generated_text"]) This fails-> It does not give me a root cause this error is all I see after it hangs for about 3 minutes INFO 05-03 23:45:17 [config.py:717] This model supports multiple tasks: {'generate', 'reward', 'classify', 'score', 'embed'}. Defaulting to 'generate'. INFO 05-03 23:45:17 [config.py:2003] Chunked prefill is enabled with max_num_batched_tokens=8192. WARNING 05-03 23:45:19 [utils.py:2382] We must use the `spawn` multiprocessing start method. Overriding VLLM_WORKER_MULTIPROC_METHOD to 'spawn'. See https://docs.vllm.ai/en/latest/getting_started/troubleshooting.html#python-multiprocessing for more information. Reason: CUDA is initialized --------------------------------------------------------------------------- Run...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: tebooks, A100 ### 🐛 Describe the bug I have no idea what's wrong. This model works with normal pipeline, but fails with vllm. It was saved to 16 bit and built off Unsloth/Llama3.18b Instruct This works -> from transform...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: oot cause above bug;stale ### Your current environment Colab notebooks, A100 ### 🐛 Describe the bug I have no idea what's wrong. This model works with normal pipeline, but fails with vllm. It was saved to 16 bit and bui...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: d built off Unsloth/Llama3.18b Instruct This works -> from transformers import pipeline prompt = ( "Do aliens suffer?" ) gen = pipeline("text-generation", model=best_model, tokenizer=tokenizer) print(gen(prompt, max_new...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: Engine Core initialization failed. See root cause above bug;stale ### Your current environment Colab notebooks, A100 ### 🐛 Describe the bug I have no idea what's wrong. This model works with normal pipeline, but...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: al pipeline, but fails with vllm. It was saved to 16 bit and built off Unsloth/Llama3.18b Instruct This works -> from transformers import pipeline prompt = ( "Do aliens suffer?" ) gen = pipeline("text-generation", model...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
