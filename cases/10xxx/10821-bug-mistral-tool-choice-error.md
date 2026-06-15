# vllm-project/vllm#10821: [Bug]: mistral tool choice error

| 字段 | 值 |
| --- | --- |
| Issue | [#10821](https://github.com/vllm-project/vllm/issues/10821) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: mistral tool choice error

### Issue 正文摘录

### Your current environment ### Model Input Dumps During handling of the above exception, another exception occurred: Traceback (most recent call last): File "/model/anaconda3/envs/vllm/lib/python3.11/site-packages/uvicorn/protocols/http/httptools_impl.py", line 401, in run_asgi result = await app( # type: ignore[func-returns-value] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/model/anaconda3/envs/vllm/lib/python3.11/site-packages/uvicorn/middleware/proxy_headers.py", line 60, in __call__ return await self.app(scope, receive, send) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/model/anaconda3/envs/vllm/lib/python3.11/site-packages/fastapi/applications.py", line 1054, in __call__ await super().__call__(scope, receive, send) File "/model/anaconda3/envs/vllm/lib/python3.11/site-packages/starlette/applications.py", line 113, in __call__ await self.middleware_stack(scope, receive, send) File "/model/anaconda3/envs/vllm/lib/python3.11/site-packages/starlette/middleware/errors.py", line 187, in __call__ raise exc File "/model/anaconda3/envs/vllm/lib/python3.11/site-packages/starlette/middleware/errors.py", line 165, in __call__ await self.app(scope, receive, _send) File "/model/a...

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: tte/middleware/base.py", line 187, in __call__ response = await self.dispatch_func(request, call_next) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/model/anaconda3/envs/vllm/lib/python3.11/site-packages/vllm/entr...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm;sampling_logits;speculative_decoding cuda;operator;sampli...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: Bug]: mistral tool choice error bug ### Your current environment ### Model Input Dumps During handling of the above exception, another exception occurred: Traceback (most recent call last): File "/model/anaconda3/envs/v...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: ge-Instruct-2411 -tp 1 --served-model-name Pixtral-Large-Instruct-2411 --dtype float16 --gpu-memory-utilization 0.925 --max-model-len 16384 --max-num-seqs 16 --tokenizer_mode mistral --enable-auto-tool-choice --tool-cal...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: 5.0 ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
