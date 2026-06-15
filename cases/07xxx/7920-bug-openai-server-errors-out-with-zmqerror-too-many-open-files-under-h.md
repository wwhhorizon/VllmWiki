# vllm-project/vllm#7920: [Bug]: OpenAI server errors out with "ZMQError Too many open files" under heavy load

| 字段 | 值 |
| --- | --- |
| Issue | [#7920](https://github.com/vllm-project/vllm/issues/7920) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: OpenAI server errors out with "ZMQError Too many open files" under heavy load

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug @robertgshaw2-neuralmagic, @njhill I am running vllm @ 665304092de6d56aaccaadacfa497a7836d88e7b which includes #7394. Reproducer: ``` # vllm serve meta-llama/Meta-Llama-3-8B-Instruct --disable-log-requests import openai import asyncio N = 800 client = openai.AsyncOpenAI(base_url="http://localhost:8000/v1", api_key="EMPTY") async def generate_streaming(prompt: str): async for req_output in await client.completions.create( model="meta-llama/Meta-Llama-3-8B-Instruct", prompt=prompt, stream=True, ): yield req_output.choices[0].text async def generate_output(prompt: str): async for output in generate_streaming(prompt): final_output = output return final_output async def main(): prompts = [str(i) for i in range(N)] async with asyncio.TaskGroup() as tg: tasks = [tg.create_task(generate_output(prompt)) for prompt in prompts] asyncio.run(main()) ``` Error message: ``` | Traceback (most recent call last): | File ".venv/lib/python3.11/site-packages/starlette/responses.py", line 261, in wrap | await func() | File ".venv/lib/python3.11/site-packages/starlette/responses.py", line 250, in stream_response | async for chunk in self.body_iterator:...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: vllm serve meta-llama/Meta-Llama-3-8B-Instruct --disable-log-requests import openai import asyncio N = 800 client = openai.AsyncOpenAI(base_url="http://localhost:8000/v1", api_key="EMPTY") async def generate_streaming(p...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: a497a7836d88e7b which includes #7394. Reproducer: ``` # vllm serve meta-llama/Meta-Llama-3-8B-Instruct --disable-log-requests import openai import asyncio N = 800 client = openai.AsyncOpenAI(base_url="http://localhost:8...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: t__ | super().__init__( | File "_zmq.py", line 690, in zmq.backend.cython._zmq.Socket.__init__ | zmq.error.ZMQError: Too many open files ``` This arguably is not normal online serving traffic. With that said, if `--disa...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: g vllm @ 665304092de6d56aaccaadacfa497a7836d88e7b which includes #7394. Reproducer: ``` # vllm serve meta-llama/Meta-Llama-3-8B-Instruct --disable-log-requests import openai import asyncio N = 800 client = openai.AsyncO...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: strace shows lots of eventfd, which might be related to https://www.mail-archive.com/zeromq-dev@lists.zeromq.org/msg31244.html ``` 730059 eventfd2(0, EFD_CLOEXEC) = 976 730059 eventfd2(0, EFD_CLOEXEC) = 977 730059 event...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
