# vllm-project/vllm#43480: [Bug]: vllm-openai nightly Docker image fails to start due to missing pytest imported via humming/cupy

| 字段 | 值 |
| --- | --- |
| Issue | [#43480](https://github.com/vllm-project/vllm/issues/43480) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: vllm-openai nightly Docker image fails to start due to missing pytest imported via humming/cupy

### Issue 正文摘录

### Your current environment https://hub.docker.com/layers/vllm/vllm-openai/nightly/images/sha256-0175610003dc9531eb853ffe77907ac9f3d49b9d2cc7ee7885195ed2697436d7 ### 🐛 Describe the bug The `vllm/vllm-openai:nightly` Docker image fails during startup before the OpenAI API server becomes ready. The failure happens while vLLM is creating the model config and verifying quantization. The import path eventually reaches `humming`, then `torch.library._register_fake`, then Python `inspect`, which unexpectedly imports `cupy.testing`. `cupy.testing` imports `pytest`, but `pytest` is not installed in the runtime Docker image. This looks like a Docker image / runtime dependency issue, or an unintended import side effect, because starting the vLLM server should not require the test dependency `pytest`. ### Docker image ```text vllm/vllm-openai:nightly Digest: sha256:0175610003dc9531eb853ffe77907ac9f3d49b9d2cc7ee7885195ed2697436d7 ``` ### vLLM version ```text 0.21.1rc1.dev243+ga5bbd81e2 ``` ### Model ```text RedHatAI/gemma-4-31B-it-NVFP4 ``` ### Startup arguments The server was started with the following non-default arguments shown in the log: ```text { 'model_tag': 'RedHatAI/gemma-4-31B-it-NV...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: [Bug]: vllm-openai nightly Docker image fails to start due to missing pytest imported via humming/cupy bug ### Your current environment https://hub.docker.com/layers/vllm/vllm-openai/nightly/images/sha256-0175610003dc95...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: he failure happens while vLLM is creating the model config and verifying quantization. The import path eventually reaches `humming`, then `torch.library._register_fake`, then Python `inspect`, which unexpectedly imports...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: PI server becomes ready. The failure happens while vLLM is creating the model config and verifying quantization. The import path eventually reaches `humming`, then `torch.library._register_fake`, then Python `inspect`,...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: edHatAI/gemma-4-31B-it-NVFP4 INFO 05-23 12:45:45 [model.py:617] Resolved architecture: Gemma4ForConditionalGeneration INFO 05-23 12:45:45 [model.py:1752] Using max model len 256000 Traceback (most recent call last): Fil...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: 2/dist-packages/vllm/entrypoints/cli/main.py", line 92, in main args.dispatch_function(args) File "/usr/local/lib/python3.12/dist-packages/vllm/entrypoints/cli/serve.py", line 148, in cmd uvloop.run(run_server(args)) Fi...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
