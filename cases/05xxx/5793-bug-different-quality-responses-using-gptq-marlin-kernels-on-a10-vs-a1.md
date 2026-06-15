# vllm-project/vllm#5793: [Bug]: Different quality responses using GPTQ / marlin kernels on A10 vs A100 GPUs

| 字段 | 值 |
| --- | --- |
| Issue | [#5793](https://github.com/vllm-project/vllm/issues/5793) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;frontend_api;hardware_porting;model_support;quantization |
| 子分类 | precision |
| Operator 关键词 | attention;fp8;kernel;quantization |
| 症状 | slowdown |
| 根因提示 | dtype |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Different quality responses using GPTQ / marlin kernels on A10 vs A100 GPUs

### Issue 正文摘录

### 🐛 Describe the bug Hello, I am running llama3-70b and mixtral with VLLM on a bunch of different kinds of machines. I encountered wildly different quality performance on A10 GPUs vs A100/H100 GPUs for ONLY gptq models and marlin kernels. GPTQ with marlin kernels is way faster than AWQ but with AWQ, i see roughly the same response on my test queries on either kind of GPU environment. For A10 deployments, the only difference in the settings is that I use 2 A10 24GB GPUs instead of 1 A100 or H100 (using the tensor parallelism param). I am running vllm = 0.4.2. I am using examples from llama3-70b testing on a very simple test query but I also saw the similar flavor of quality issues with mixtral-awq vs mixtral-gptq as well and I also saw the same flavor of issues on all my other more complicated RAG test queries as well. Generally the gptq models on A10s are psychotic and unusable and behave as if the model files are screwed up, which is why i tested two publicly available quantizations of llama3... I also tried to simulate a GPU environment of 2 A10s on 1 single A100 by setting --gpu-memory-utilization to 0.55 i.e. I choked the vram on the A100 deployment to choke the kv-cache ava...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: [Bug]: Different quality responses using GPTQ / marlin kernels on A10 vs A100 GPUs bug ### 🐛 Describe the bug Hello, I am running llama3-70b and mixtral with VLLM on a bunch of different kinds of machines. I encountered...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: ls on A10 vs A100 GPUs bug ### 🐛 Describe the bug Hello, I am running llama3-70b and mixtral with VLLM on a bunch of different kinds of machines. I encountered wildly different quality performance on A10 GPUs vs A100/H1...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: model files are screwed up, which is why i tested two publicly available quantizations of llama3... I also tried to simulate a GPU environment of 2 A10s on 1 single A100 by setting --gpu-memory-utilization to 0.55 i.e....
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: way faster than AWQ but with AWQ, i see roughly the same response on my test queries on either kind of GPU environment. For A10 deployments, the only difference in the settings is that I use 2 A10 24GB GPUs instead of 1...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: my model uses a technique called "knowledge distillation" to reduce the precision of my weights and activations while maintaining the accuracy of my responses. Knowledge distillation is a method that involves training a...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
