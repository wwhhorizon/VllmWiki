# vllm-project/vllm#33001: [Bug] [CPU Backend]: Failed to import from vllm._C with torch 2.10 on Darwin

| 字段 | 值 |
| --- | --- |
| Issue | [#33001](https://github.com/vllm-project/vllm/issues/33001) |
| 状态 | closed |
| 标签 | bug;cpu |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug] [CPU Backend]: Failed to import from vllm._C with torch 2.10 on Darwin

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Reproducer: 1. Build vLLM on Darwin system with torch 2.10 (you need to add that to `requirements/cpu.txt`) ``` uv pip install -r requirements/cpu.txt --index-strategy unsafe-best-match uv pip install -e . ``` 2. Run: `vllm bench throughput --input_len 32 --max_model_len 1024` And you'll see this error: ``` WARNING 01-23 13:15:46 [interface.py:222] Failed to import from vllm._C: ImportError('dlopen(/Users/runner/work/vllm/vllm/vllm/_C.abi3.so, 0x0002): Symbol not found: __ZN3c1013MessageLoggerC1EPKcii\n Referenced from: /Users/runner/work/vllm/vllm/vllm/_C.abi3.so\n Expected in: /Users/runner/work/vllm/vllm/.venv/lib/python3.12/site-packages/torch/lib/libc10.dylib') ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: [Bug] [CPU Backend]: Failed to import from vllm._C with torch 2.10 on Darwin bug;cpu ### Your current environment ### 🐛 Describe the bug Reproducer: 1. Build vLLM on Darwin system with torch 2.10 (you need to add that t...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: strategy unsafe-best-match uv pip install -e . ``` 2. Run: `vllm bench throughput --input_len 32 --max_model_len 1024` And you'll see this error: ``` WARNING 01-23 13:15:46 [interface.py:222] Failed to import from vllm....
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: [Bug] [CPU Backend]: Failed to import from vllm._C with torch 2.10 on Darwin bug;cpu ### Your current environment ### 🐛 Describe the bug Reproducer: 1. Build vLLM on Darwin system with torch 2.10 (you need to add that t...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: Darwin bug;cpu ### Your current environment ### 🐛 Describe the bug Reproducer: 1. Build vLLM on Darwin system with torch 2.10 (you need to add that to `requirements/cpu.txt`) ``` uv pip install -r requirements/cpu.txt -...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
