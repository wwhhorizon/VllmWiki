# vllm-project/vllm#1716: ImportError: libcudart.so.12: cannot open shared object file: No such file or directory

| 字段 | 值 |
| --- | --- |
| Issue | [#1716](https://github.com/vllm-project/vllm/issues/1716) |
| 状态 | closed |
| 标签 |  |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> ImportError: libcudart.so.12: cannot open shared object file: No such file or directory

### Issue 正文摘录

My code work well yesterday but now it is not working today since the latest update (v.0.2.2)! My code: ```python from langchain.llms import VLLM llm = VLLM( model=GENERATE_MODEL_NAME, trust_remote_code=True, # mandatory for hf models max_new_tokens=max_new_tokens, top_k=10, top_p=0.95, temperature=0.8, # dtype="half", vllm_kwargs={"quantization": "awq"} ) ``` The error: ``` ImportError: libcudart.so.12: cannot open shared object file: No such file or directory During handling of the above exception, another exception occurred: ImportError Traceback (most recent call last) [/usr/local/lib/python3.10/dist-packages/langchain/llms/vllm.py](https://localhost:8080/#) in validate_environment(cls, values) 79 from vllm import LLM as VLLModel 80 except ImportError: ---> 81 raise ImportError( 82 "Could not import vllm python package. " 83 "Please install it with `pip install vllm`." ImportError: Could not import vllm python package. Please install it with `pip install vllm`. ``` I tried 'pip install vllm' many time but not fixed. I run on my Google Colab T4. Anyone has the same issue?

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: ImportError: libcudart.so.12: cannot open shared object file: No such file or directory My code work well yesterday but now it is not working today since the latest update (v.0.2.2)! My code: ```python from langchain.llm
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: max_new_tokens, top_k=10, top_p=0.95, temperature=0.8, # dtype="half", vllm_kwargs={"quantization": "awq"} ) ``` The error: ``` ImportError: libcudart.so.12: cannot open shared object file: No such file or directory Dur...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: 2.2)! My code: ```python from langchain.llms import VLLM llm = VLLM( model=GENERATE_MODEL_NAME, trust_remote_code=True, # mandatory for hf models max_new_tokens=max_new_tokens, top_k=10, top_p=0.95, temperature=0.8, # d...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ImportError: libcudart.so.12: cannot open shared object file: No such file or directory My code work well yesterday but now it is not working today since the latest update (v.0.2.2)! My code: ```python from langchain.ll...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: My code work well yesterday but now it is not working today since the latest update (v.0.2.2)! My code: ```python from langchain.llms import VLLM llm = VLLM( model=GENERATE_MODEL_NAME, trust_remote_code=True, # mandator...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
