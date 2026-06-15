# vllm-project/vllm#28107: [Bug]: llama 4 + fp4 is broke

| 字段 | 值 |
| --- | --- |
| Issue | [#28107](https://github.com/vllm-project/vllm/issues/28107) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;model_support;quantization |
| 子分类 | precision |
| Operator 关键词 | quantization |
| 症状 |  |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: llama 4 + fp4 is broke

### Issue 正文摘录

### Your current environment Hi, the accuracy is not expected. docker run --runtime nvidia --gpus all \ -v ~/.cache/huggingface:/root/.cache/huggingface \ --env "HUGGING_FACE_HUB_TOKEN=$HF_TOKEN" \ -p 8000:8000 \ --ipc=host \ vllm/vllm-openai:latest \ --model nvidia/Llama-4-Scout-17B-16E-Instruct-FP4 \ --tensor-parallel-size 8 \ --quantization modelopt ### 🐛 Describe the bug b200 lm_eval --model local-chat-completions --model_args model=nvidia/Llama-4-Scout-17B-16E-Instruct-FP4,base_url=http://0.0.0.0:8000/v1/chat/completions,num_concurrent=512,timeout=999999,max_gen_toks=2048 --tasks mmlu_pro --batch_size 512 --apply_chat_template --num_fewshot 0 It should be 0.75 . local-chat-completions (model=nvidia/Llama-4-Scout-17B-16E-Instruct-FP4,base_url=http://0.0.0.0:8000/v1/chat/completions,num_concurrent=512,timeout=999999,max_gen_toks=2048), gen_kwargs: (None), limit: None, num_fewshot: 0, batch_size: 512 | Tasks |Version| Filter |n-shot| Metric | |Value | |Stderr| |-------------------|------:|--------------|-----:|-----------|---|-----:|---|-----:| |mmlu_pro | 2.0|custom-extract| |exact_match|↑ |0.5071|± |0.0045| | - biology | 2.1|custom-extract| 0|exact_match|↑ |0.7364|± |0.0165| |...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: g;stale ### Your current environment Hi, the accuracy is not expected. docker run --runtime nvidia --gpus all \ -v ~/.cache/huggingface:/root/.cache/huggingface \ --env "HUGGING_FACE_HUB_TOKEN=$HF_TOKEN" \ -p 8000:8000...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: llama 4 + fp4 is broke bug;stale ### Your current environment Hi, the accuracy is not expected. docker run --runtime nvidia --gpus all \ -v ~/.cache/huggingface:/root/.cache/huggingface \ --env "HUGGING_FACE_HU
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: : llama 4 + fp4 is broke bug;stale ### Your current environment Hi, the accuracy is not expected. docker run --runtime nvidia --gpus all \ -v ~/.cache/huggingface:/root/.cache/huggingface \ --env "HUGGING_FACE_HUB_TOKEN...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: [Bug]: llama 4 + fp4 is broke bug;stale ### Your current environment Hi, the accuracy is not expected. docker run --runtime nvidia --gpus all \ -v ~/.cache/huggingface:/root/.cache/huggingface \ --env "HUGGING_FACE_HUB_...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: r-parallel-size 8 \ --quantization modelopt ### 🐛 Describe the bug b200 lm_eval --model local-chat-completions --model_args model=nvidia/Llama-4-Scout-17B-16E-Instruct-FP4,base_url=http://0.0.0.0:8000/v1/chat/completion...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
