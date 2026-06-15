# vllm-project/vllm#15809: [Performance]: Why AWQ model‘s performance issue on A100&H100

| 字段 | 值 |
| --- | --- |
| Issue | [#15809](https://github.com/vllm-project/vllm/issues/15809) |
| 状态 | closed |
| 标签 | performance;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | distributed_parallel;gemm_linear;model_support;quantization |
| 子分类 | latency_reg |
| Operator 关键词 | gemm;quantization |
| 症状 |  |
| 根因提示 | env_dependency;memory_layout;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Performance]: Why AWQ model‘s performance issue on A100&H100

### Issue 正文摘录

### Misc discussion on performance I am using 0.8.3 version of vllm,driver 570.124.06, this command to serve to depoly AWQ model casperhansen/llama-3.3-70b-instruct-awq （GEMM） on single H100PCIE & single A100 PCIE python -m vllm.entrypoints.openai.api_server --model casperhansen/llama-3.3-70b-instruct-awq --max-num-seqs=256 --max-model-len=4096 --max-num-batched-tokens=4096 --tensor-parallel-size=1 --block-size=128 --host=0.0.0.0 --port=8000 --gpu-memory-utilization=0.9 --trust-remote-code We run the test with 2048 input and output, on batch size 1,2,4,8,32,64, and we find H100 just little better than A00 about 10-30% on TTFT and TPOT almost all batch size. However on GPTQ model (w4a16). the perofromance is very different. H100 is 2 times better than A100. So my question is what is going on with AWQ quantized model? Why AWQ model on H100 is not 2time better than A100 as GPTQ model, they both Q4A16, should have similar performance? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: 0 performance;stale ### Misc discussion on performance I am using 0.8.3 version of vllm,driver 570.124.06, this command to serve to depoly AWQ model casperhansen/llama-3.3-70b-instruct-awq （GEMM） on single H100PCIE & si...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Performance]: Why AWQ model‘s performance issue on A100&H100 performance;stale ### Misc discussion on performance I am using 0.8.3 version of vllm,driver 570.124.06, this command to serve to depoly AWQ model casperhans...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: -model-len=4096 --max-num-batched-tokens=4096 --tensor-parallel-size=1 --block-size=128 --host=0.0.0.0 --port=8000 --gpu-memory-utilization=0.9 --trust-remote-code We run the test with 2048 input and output, on batch si...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Performance]: Why AWQ model‘s performance issue on A100&H100 performance;stale ### Misc discussion on performance I am using 0.8.3 version of vllm,driver 570.124.06, this command to serve to depoly AWQ model casperhans...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: port=8000 --gpu-memory-utilization=0.9 --trust-remote-code We run the test with 2048 input and output, on batch size 1,2,4,8,32,64, and we find H100 just little better than A00 about 10-30% on TTFT and TPOT almost all b...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
