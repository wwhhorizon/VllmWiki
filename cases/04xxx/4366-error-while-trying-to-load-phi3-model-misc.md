# vllm-project/vllm#4366: Error while trying to load phi3 model [Misc]: 

| 字段 | 值 |
| --- | --- |
| Issue | [#4366](https://github.com/vllm-project/vllm/issues/4366) |
| 状态 | closed |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Error while trying to load phi3 model [Misc]: 

### Issue 正文摘录

### Anything you want to discuss about vllm. Getting the model `Azma-AI/azma-phi-3-mini-3b-128k-250424` from hugging face config.json: 100%|████████████████████████████████████| 3.43k/3.43k [00:00 sys.exit(main()) File "/root/.cache/pypoetry/virtualenvs/azma-xS3fZVNL-py3.10/lib/python3.10/site-packages/click/core.py", line 1157, in __call__ return self.main(*args, **kwargs) File "/root/.cache/pypoetry/virtualenvs/azma-xS3fZVNL-py3.10/lib/python3.10/site-packages/click/core.py", line 1078, in main rv = self.invoke(ctx) File "/root/.cache/pypoetry/virtualenvs/azma-xS3fZVNL-py3.10/lib/python3.10/site-packages/click/core.py", line 1434, in invoke return ctx.invoke(self.callback, **ctx.params) File "/root/.cache/pypoetry/virtualenvs/azma-xS3fZVNL-py3.10/lib/python3.10/site-packages/click/core.py", line 783, in invoke return __callback(*args, **kwargs) File "/root/.cache/pypoetry/virtualenvs/azma-xS3fZVNL-py3.10/lib/python3.10/site-packages/uvicorn/main.py", line 418, in main run( File "/root/.cache/pypoetry/virtualenvs/azma-xS3fZVNL-py3.10/lib/python3.10/site-packages/uvicorn/main.py", line 587, in run server.run() File "/root/.cache/pypoetry/virtualenvs/azma-xS3fZVNL-py3.10/lib/python...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: Error while trying to load phi3 model [Misc]: ### Anything you want to discuss about vllm. Getting the model `Azma-AI/azma-phi-3-mini-3b-128k-250424` from hugging face config.json: 100%|█████████████████████████████████...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: hon3.10/site-packages/uvicorn/server.py", line 62, in run return asyncio.run(self.serve(sockets=sockets)) File "/usr/lib/python3.10/asyncio/runners.py", line 44, in run return loop.run_until_complete(main) File "uvloop/...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: kspace/azma/main.py", line 6, in from routes.language_route import router as llm_router File "/workspace/azma/routes/language_route.py", line 6, in from language_models import AZMA_LANGUAGE_MODEL File "/workspace/azma/l...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
