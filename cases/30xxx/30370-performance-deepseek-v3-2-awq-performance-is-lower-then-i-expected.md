# vllm-project/vllm#30370: [Performance]: DeepSeek-V3.2 AWQ Performance is lower then i expected

| 字段 | 值 |
| --- | --- |
| Issue | [#30370](https://github.com/vllm-project/vllm/issues/30370) |
| 状态 | closed |
| 标签 | performance;stale |
| 评论 | 21; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | distributed_parallel;frontend_api;model_support;quantization |
| 子分类 | kernel_eff |
| Operator 关键词 | quantization |
| 症状 |  |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Performance]: DeepSeek-V3.2 AWQ Performance is lower then i expected

### Issue 正文摘录

### Proposal to improve performance When performing a performance test on deepseek v3.2 AWQ https://huggingface.co/QuantTrio/DeepSeek-V3.2-AWQ under the conditions below, it was found that the performance was lower than that of the existing deepseek v3 in the input 10k output 2k token section. Additionally, if you set the VLLM_USE_DEEP_GEMM environment variable to 0, VLLM will die immediately after inference. Did I do something wrong with my settings? Or is this the performance of the current version of vllm? ### Report of performance regression _No response_ ### Misc discussion on performance _No response_ ### Your current environment (if you think it is necessary) Model: https://huggingface.co/QuantTrio/DeepSeek-V3.2-AWQ GPU: H100 * 8 VLLM Version: nightly(pull 12/08) VLLM Parameter: - --load-format - auto - --max-model-len - "65536" - --gpu-memory-utilization - "0.9" - --prefix-caching-hash-algo - sha256 - --enable-prefix-caching - --uvicorn-log-level - warning - --disable-log-requests - --port - "8080" - --trust-remote-code - --enable-auto-tool-choice - --tokenizer-mode - "deepseek_v32" - --tool-call-parser - "deepseek_v32" - --reasoning-parser - "deepseek_v3" - --tensor-paral...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ormance When performing a performance test on deepseek v3.2 AWQ https://huggingface.co/QuantTrio/DeepSeek-V3.2-AWQ under the conditions below, it was found that the performance was lower than that of the existing deepse...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: cessary) Model: https://huggingface.co/QuantTrio/DeepSeek-V3.2-AWQ GPU: H100 * 8 VLLM Version: nightly(pull 12/08) VLLM Parameter: - --load-format - auto - --max-model-len - "65536" - --gpu-memory-utilization - "0.9" -...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: nce]: DeepSeek-V3.2 AWQ Performance is lower then i expected performance;stale ### Proposal to improve performance When performing a performance test on deepseek v3.2 AWQ https://huggingface.co/QuantTrio/DeepSeek-V3.2-A...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: stale ### Proposal to improve performance When performing a performance test on deepseek v3.2 AWQ https://huggingface.co/QuantTrio/DeepSeek-V3.2-AWQ under the conditions below, it was found that the performance was lowe...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: thing wrong with my settings? Or is this the performance of the current version of vllm? ### Report of performance regression _No response_ ### Misc discussion on performance _No response_ ### Your current environment (...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
