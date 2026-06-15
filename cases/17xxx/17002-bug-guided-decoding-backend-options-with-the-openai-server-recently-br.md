# vllm-project/vllm#17002: [Bug]: Guided Decoding Backend options with the OpenAI server recently broken

| 字段 | 值 |
| --- | --- |
| Issue | [#17002](https://github.com/vllm-project/vllm/issues/17002) |
| 状态 | closed |
| 标签 | bug;structured-output |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;frontend_api |
| 子分类 | install |
| Operator 关键词 | cuda |
| 症状 |  |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Guided Decoding Backend options with the OpenAI server recently broken

### Issue 正文摘录

### Your current environment vLLM installed with: ``` pip install https://wheels.vllm.ai/5536b30a4c7877d75758d21bdaf39b3a59aa2dc2/vllm-1.0.0.dev-cp38-abi3-manylinux1_x86_64.whl ``` ### 🐛 Describe the bug After merging https://github.com/vllm-project/vllm/pull/16789, using "options" for guided decoding backends no longer works. Attempting to include a backend option results in: ``` $ vllm serve meta-llama/Llama-3.2-3B-Instruct --guided-decoding-backend xgrammar:disable-any-whitespace INFO 04-22 18:45:12 [__init__.py:239] Automatically detected platform cuda. usage: vllm serve [model_tag] [options] vllm serve: error: argument --guided-decoding-backend: invalid choice: 'xgrammar:disable-any-whitespace' (choose from 'auto', 'outlines', 'lm-format-enforcer', 'xgrammar') ``` The new type checking of the args checks against a Literal type for the backend name, disallowing any options. For reference, backend options are briefly documented [REF](https://docs.vllm.ai/en/latest/features/structured_outputs.html): > Additional backend-specific options can be supplied in a comma separated list following a colon after the backend name. For example "xgrammar:no-fallback" will not allow vLLM to fa...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: recently broken bug;structured-output ### Your current environment vLLM installed with: ``` pip install https://wheels.vllm.ai/5536b30a4c7877d75758d21bdaf39b3a59aa2dc2/vllm-1.0.0.dev-cp38-abi3-manylinux1_x86_64.whl ```...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: Attempting to include a backend option results in: ``` $ vllm serve meta-llama/Llama-3.2-3B-Instruct --guided-decoding-backend xgrammar:disable-any-whitespace INFO 04-22 18:45:12 [__init__.py:239] Automatically detected...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: [Bug]: Guided Decoding Backend options with the OpenAI server recently broken bug;structured-output ### Your current environment vLLM installed with: ``` pip install https://wheels.vllm.ai/5536b30a4c7877d75758d21bdaf39b...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ce INFO 04-22 18:45:12 [__init__.py:239] Automatically detected platform cuda. usage: vllm serve [model_tag] [options] vllm serve: error: argument --guided-decoding-backend: invalid choice: 'xgrammar:disable-any-whitesp...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: , backend options are briefly documented [REF](https://docs.vllm.ai/en/latest/features/structured_outputs.html): > Additional backend-specific options can be supplied in a comma separated list following a colon after th...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
