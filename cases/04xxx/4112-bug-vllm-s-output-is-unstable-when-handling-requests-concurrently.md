# vllm-project/vllm#4112: [Bug]: VLLM's output is unstable when handling requests CONCURRENTLY.

| 字段 | 值 |
| --- | --- |
| Issue | [#4112](https://github.com/vllm-project/vllm/issues/4112) |
| 状态 | closed |
| 标签 | bug;unstale |
| 评论 | 12; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: VLLM's output is unstable when handling requests CONCURRENTLY.

### Issue 正文摘录

### Your current environment using lastest docker images: command: docker run --runtime nvidia --gpus all -v /mnt_1/models:/models -p 8000:8000 --ipc=host vllm/vllm-openai:latest --model /models/Qwen/Qwen1.5-14B-Chat --served-model-name Qwen --gpu-memory-utilization 0.99 --max-model-len 8192 --tensor-parallel-size 1 --seed 42 ### 🐛 Describe the bug I generated 10 results concurrently by following code. But I got different results with temperate= 0 eventhough most of them are the same. ```python from langchain.llms.openai import OpenAI import multiprocessing llm = OpenAI( openai_api_key="EMPTY", openai_api_base="http://127.0.0.1:8000/v1", model_name="Qwen", temperature=0, max_tokens=1024, stop=[' ', ' ', ' '], ) prompt_template = \ """ system You are a helpful assistant. user {query} assistant """ def main(prompt): return llm(prompt) if __name__ == '__main__': # results from concurrent requests are unstable prompt = prompt_template.format_map({'query': '写500字关于富春山居图的文章。'}) with multiprocessing.Pool(10) as pool: res = pool.map(main, [prompt]*10) for i, x in enumerate(res): print(f'==={i}===') print(x) ``` following are the printed results: ``` ===0=== 《富春山居图》，是中国十大传世名画之一，是元代大画家黄公望的代...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ocker images: command: docker run --runtime nvidia --gpus all -v /mnt_1/models:/models -p 8000:8000 --ipc=host vllm/vllm-openai:latest --model /models/Qwen/Qwen1.5-14B-Chat --served-model-name Qwen --gpu-memory-utilizat...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: ts CONCURRENTLY. bug;unstale ### Your current environment using lastest docker images: command: docker run --runtime nvidia --gpus all -v /mnt_1/models:/models -p 8000:8000 --ipc=host vllm/vllm-openai:latest --model /mo...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: VLLM's output is unstable when handling requests CONCURRENTLY. bug;unstale ### Your current environment using lastest docker images: command: docker run --runtime nvidia --gpus all -v /mnt_1/models:/models -p 800...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: equests CONCURRENTLY. bug;unstale ### Your current environment using lastest docker images: command: docker run --runtime nvidia --gpus all -v /mnt_1/models:/models -p 8000:8000 --ipc=host vllm/vllm-openai:latest --mode...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
