# vllm-project/vllm#35962: [RFC]: Add PPL and KLD to VLLM

| 字段 | 值 |
| --- | --- |
| Issue | [#35962](https://github.com/vllm-project/vllm/issues/35962) |
| 状态 | open |
| 标签 | RFC;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Add PPL and KLD to VLLM

### Issue 正文摘录

### Motivation. In the enterprise space, Evals reign supreme, and are aligned to specific work outcomes. In the consumer/prosumer space, PPL and KLD are really important for good general alignment on how good a Quant is. Exllama3 has PPL and llama.cpp has PPL and KLD. Exllama3 has done a great job in his approach to doing PPL via evaluating every single position in every single window. Llama.cpp's implementation is lacking, both in their context and their stride. I think having the ability to easily see KLD on models produced from llm_compressor and model_opt would help people better understand all the tunings of AWQ(Group size, Datasets, Samples and Sequence Lengths), GPTQ, NVFP4 (PTQ, QAT, and QAD), etc. Turbo of EXLlama3 was awesome and helped explain to me how his logic works, as it relates to windows, context, etc. I then copied his approach and applied it into VLLM. Both PPL and KLD are now available in my branch. ### Proposed Change. See my draft PR here: https://github.com/vllm-project/vllm/pull/35961 ### Feedback Period. _No response_ ### CC List. _No response_ ### Any Other Things. _No response_ ### Before submitting a new issue... - [x] Make sure you already searched fo...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: PL and KLD are really important for good general alignment on how good a Quant is. Exllama3 has PPL and llama.cpp has PPL and KLD. Exllama3 has done a great job in his approach to doing PPL via evaluating every single p...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: on. In the enterprise space, Evals reign supreme, and are aligned to specific work outcomes. In the consumer/prosumer space, PPL and KLD are really important for good general alignment on how good a Quant is. Exllama3 h...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: e really important for good general alignment on how good a Quant is. Exllama3 has PPL and llama.cpp has PPL and KLD. Exllama3 has done a great job in his approach to doing PPL via evaluating every single position in ev...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [RFC]: Add PPL and KLD to VLLM RFC;stale ### Motivation. In the enterprise space, Evals reign supreme, and are aligned to specific work outcomes. In the consumer/prosumer space, PPL and KLD are really important for good...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: PPL and KLD to VLLM RFC;stale ### Motivation. In the enterprise space, Evals reign supreme, and are aligned to specific work outcomes. In the consumer/prosumer space, PPL and KLD are really important for good general al...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
