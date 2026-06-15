# vllm-project/vllm#1266: [Model support request] Support for PolyLM

| 字段 | 值 |
| --- | --- |
| Issue | [#1266](https://github.com/vllm-project/vllm/issues/1266) |
| 状态 | closed |
| 标签 | new-model;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Model support request] Support for PolyLM

### Issue 正文摘录

I would be really grateful if you could add support for the PolyLM model to vLLM. PolyLLM paper: https://arxiv.org/pdf/2307.06018.pdf PolyLLM weights on HF: https://huggingface.co/DAMO-NLP-MT/polylm-13b I think it could be a really important addition as it is one of the first explicitly multilingual LLMs that has shown competitive performance on benchmarks compared to other SOTA baseline models. If the PolyLM architecture was supported on vLLM, it could potentially be used by many many more people looking to use language models not in either English or Chinese. Thanks.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Model support request] Support for PolyLM new-model;stale I would be really grateful if you could add support for the PolyLM model to vLLM. PolyLLM paper: https://arxiv.org/pdf/2307.06018.pdf PolyLLM weights on HF: http
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: ps://huggingface.co/DAMO-NLP-MT/polylm-13b I think it could be a really important addition as it is one of the first explicitly multilingual LLMs that has shown competitive performance on benchmarks compared to other SO...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Model support request] Support for PolyLM new-model;stale I would be really grateful if you could add support for the PolyLM model to vLLM. PolyLLM paper: https://arxiv.org/pdf/2307.06018.pdf PolyLLM weights on HF: htt...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ance on benchmarks compared to other SOTA baseline models. If the PolyLM architecture was supported on vLLM, it could potentially be used by many many more people looking to use language models not in either English or...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: t explicitly multilingual LLMs that has shown competitive performance on benchmarks compared to other SOTA baseline models. If the PolyLM architecture was supported on vLLM, it could potentially be used by many many mor...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
