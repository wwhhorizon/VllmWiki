# vllm-project/vllm#9051: [Usage]: Tried using vllm with GGUF models. Got an infer device type error.

| 字段 | 值 |
| --- | --- |
| Issue | [#9051](https://github.com/vllm-project/vllm/issues/9051) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Tried using vllm with GGUF models. Got an infer device type error.

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` CODE: from langchain.llms import VLLM import time import uvicorn app = FastAPI() llm = VLLM(model="tiiuae/falcon-7b-instruct", trust_remote_code=True, # mandatory for hf models max_new_tokens=50, temperature=0.6 ) @app.get("/") def read_root(): return {"Hello": "World"} @app.post("/v1/generateText") async def generateText(request: Request) -> Response: request_dict = await request.json() prompt = request_dict.pop("prompt") print(prompt) output = llm(prompt) print("Generated text:", output) ret = {"text": output} return JSONResponse(ret) ERROR:WARNING 10-03 20:16:19 _custom_ops.py:18] Failed to import from vllm._C with ImportError('libcuda.so.1: cannot open shared object file: No such file or directory') Traceback (most recent call last): File "/home/ubuntu/llm/app1.py", line 35, in llm = LLM(model="llama-2-7b-chat.Q5_K_S.gguf") ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/home/ubuntu/llm/myenv/lib/python3.12/site-packages/vllm/entrypoints/llm.py", line 214, in __init__ self.llm_engine = LLMEngine.from_engine_args( ^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/home/ubuntu/llm/myenv/lib/python3.12/site-packages/v...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Usage]: Tried using vllm with GGUF models. Got an infer device type error. usage;stale ### Your current environment ```text The output of `python collect_env.py` ``` CODE: from langchain.llms import VLLM import time im...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: 19 _custom_ops.py:18] Failed to import from vllm._C with ImportError('libcuda.so.1: cannot open shared object file: No such file or directory') Traceback (most recent call last): File "/home/ubuntu/llm/app1.py", line 35...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: Tried using vllm with GGUF models. Got an infer device type error. usage;stale ### Your current environment ```text The output of `python collect_env.py` ``` CODE: from langchain.llms import VLLM import time import uvic...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: xt The output of `python collect_env.py` ``` CODE: from langchain.llms import VLLM import time import uvicorn app = FastAPI() llm = VLLM(model="tiiuae/falcon-7b-instruct", trust_remote_code=True, # mandatory for hf mode...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
