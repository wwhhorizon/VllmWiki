# vllm-project/vllm#8807: [Bug]: Decrease generation quality Mixtral

| 字段 | 值 |
| --- | --- |
| Issue | [#8807](https://github.com/vllm-project/vllm/issues/8807) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support |
| 子分类 | kernel_eff |
| Operator 关键词 | cuda |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Decrease generation quality Mixtral

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug After updating from v0.3.3 to 0.6.1post1 I got the impression that the quality of the model Nous-Hermes-2-Mixtral-8x7B-DPO got worse. Inspired by #8747 I ran lm-eval against both versions. ``` lm_eval --model local-chat-completions --model_args model=/secondary/thies/Nous-Hermes-2-Mixtral-8x7B-DPO/,base_url=http://localhost:8000/v1/chat/completions,num_concurrent=30,max_retries=3,tokenized_requests=False --tasks gsm8k --apply_chat_template ``` v0.3.3: ``` |Tasks|Version| Filter |n-shot| Metric | |Value | |Stderr| |-----|------:|----------------|-----:|-----------|---|-----:|---|-----:| |gsm8k| 3|flexible-extract| 5|exact_match|↑ |0.7680|± |0.0116| | | |strict-match | 5|exact_match|↑ |0.7597|± |0.0118| ``` v0.6.1post1: ``` |Tasks|Version| Filter |n-shot| Metric | |Value | |Stderr| |-----|------:|----------------|-----:|-----------|---|-----:|---|-----:| |gsm8k| 3|flexible-extract| 5|exact_match|↑ |0.1175|± |0.0089| | | |strict-match | 5|exact_match|↑ |0.1152|± |0.0088| ``` vllm options are for both cases: ``` --tensor-parallel-size 8 --max-num-batched-tokens 32768 --gpu-memory-utilization 0.85 `...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: Mixtral-8x7B-DPO got worse. Inspired by #8747 I ran lm-eval against both versions. ``` lm_eval --model local-chat-completions --model_args model=/secondary/thies/Nous-Hermes-2-Mixtral-8x7B-DPO/,base_url=http://localhost...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: etions,num_concurrent=30,max_retries=3,tokenized_requests=False --tasks gsm8k --apply_chat_template ``` v0.3.3: ``` |Tasks|Version| Filter |n-shot| Metric | |Value | |Stderr| |-----|------:|----------------|-----:|-----...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: del Nous-Hermes-2-Mixtral-8x7B-DPO got worse. Inspired by #8747 I ran lm-eval against both versions. ``` lm_eval --model local-chat-completions --model_args model=/secondary/thies/Nous-Hermes-2-Mixtral-8x7B-DPO/,base_ur...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: v1/chat/completions,num_concurrent=30,max_retries=3,tokenized_requests=False --tasks gsm8k --apply_chat_template ``` v0.3.3: ``` |Tasks|Version| Filter |n-shot| Metric | |Value | |Stderr| |-----|------:|----------------...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ease generation quality Mixtral bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug After updating from v0.3.3 to 0.6.1post1 I got the impression that the quality of the model Nou...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
