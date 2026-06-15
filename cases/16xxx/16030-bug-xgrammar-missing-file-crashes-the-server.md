# vllm-project/vllm#16030: [Bug]: xgrammar missing file crashes the server

| 字段 | 值 |
| --- | --- |
| Issue | [#16030](https://github.com/vllm-project/vllm/issues/16030) |
| 状态 | closed |
| 标签 | bug;structured-output |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: xgrammar missing file crashes the server

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I have the following xgrammar version ``` [root@~]# pip show xgrammar Name: xgrammar Version: 0.1.17 Summary: Efficient, Flexible and Portable Structured Generation Home-page: https://xgrammar.mlc.ai/ Author: MLC Team Author-email: License: Apache 2.0 Location: /opt/pytorch/lib/python3.12/site-packages Requires: nanobind, ninja, pydantic, sentencepiece, tiktoken, torch, transformers Required-by: vllm ``` and this is the command I use to initialize the model ``` /opt/pytorch/bin/vllm serve Mistral/ --tokenizer_mode mistral --config_format mistral --load_format mistral --tool-call-parser mistral --enable-auto-tool-choice --limit_mm_per_prompt 'image=1' --tensor-parallel-size 4 --max-model-len 120000 --quantization fp8 --port 8006 --host localhost --guided-decoding-backend xgrammar ``` The model is `mistralai/Mistral-Small-3.1-24B-Instruct-2503` However, whenever I try to send a request with xgrammar as a request param I get the following error and the server crashes after this ``` Apr 3 17:38:52 langmodel52 langmodel[139935]: 2025-04-03 17:38:52,710 - vllm.v1.metrics.loggers - INFO - Avg prompt throughput: 0.0 tokens/s, Avg generat...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: nt environment ### 🐛 Describe the bug I have the following xgrammar version ``` [root@~]# pip show xgrammar Name: xgrammar Version: 0.1.17 Summary: Efficient, Flexible and Portable Structured Generation Home-page: https...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: t --guided-decoding-backend xgrammar ``` The model is `mistralai/Mistral-Small-3.1-24B-Instruct-2503` However, whenever I try to send a request with xgrammar as a request param I get the following error and the server c...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: rs Required-by: vllm ``` and this is the command I use to initialize the model ``` /opt/pytorch/bin/vllm serve Mistral/ --tokenizer_mode mistral --config_format mistral --load_format mistral --tool-call-parser mistral -...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: /Mistral-Small-3.1-24B-Instruct-2503` However, whenever I try to send a request with xgrammar as a request param I get the following error and the server crashes after this ``` Apr 3 17:38:52 langmodel52 langmodel[13993...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: m_per_prompt 'image=1' --tensor-parallel-size 4 --max-model-len 120000 --quantization fp8 --port 8006 --host localhost --guided-decoding-backend xgrammar ``` The model is `mistralai/Mistral-Small-3.1-24B-Instruct-2503`...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
