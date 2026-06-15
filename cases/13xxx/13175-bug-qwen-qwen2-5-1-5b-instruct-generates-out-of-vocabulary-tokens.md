# vllm-project/vllm#13175: [Bug]: Qwen/Qwen2.5-1.5B-Instruct generates out of vocabulary tokens

| 字段 | 值 |
| --- | --- |
| Issue | [#13175](https://github.com/vllm-project/vllm/issues/13175) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 39; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | frontend_api;model_support;sampling_logits |
| 子分类 | debug |
| Operator 关键词 | cuda |
| 症状 |  |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Qwen/Qwen2.5-1.5B-Instruct generates out of vocabulary tokens

### Issue 正文摘录

### Your current environment ```python >>> import vllm INFO 02-12 20:27:04 __init__.py:190] Automatically detected platform cuda. >>> vllm.__version__ '0.7.2' ``` ### 🐛 Describe the bug Hi, It looks like Qwen models can generate tokens out of vocabulary. We can see this by feeding the generate tokens to the model which sometimes result in the following exception: `Token id 151779 is out of vocabulary`. Here is a minimal code to reproduce this error. ```python import vllm from transformers import AutoTokenizer import numpy as np PROMPT = """ system Please reason step by step, and put your final answer within \\boxed{}. user The equation $a^7xy-a^6y-a^5x=a^4(b^4-1)$ is equivalent to the equation $(a^mx-a^n)(a^py-a^2)=a^4b^4$ for some integers $m$, $n$, and $p$. Find $mnp$. assistant """ if __name__ == '__main__': model_path = "Qwen/Qwen2.5-1.5B-Instruct" tokenizer = AutoTokenizer.from_pretrained(model_path) PROMPT_TOKEN_IDS = tokenizer.encode(PROMPT) sampling_params = vllm.SamplingParams(temperature=1.2, max_tokens=100) llm = vllm.LLM(model_path) # can we now generate tokens out of vocabulary? out_of_vocab = [] out_of_vocab_tokens = [] for i in range(100): out = llm.generate(prompt_...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: vocabulary tokens bug;stale ### Your current environment ```python >>> import vllm INFO 02-12 20:27:04 __init__.py:190] Automatically detected platform cuda. >>> vllm.__version__ '0.7.2' ``` ### 🐛 Describe the bug Hi, I...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: llm INFO 02-12 20:27:04 __init__.py:190] Automatically detected platform cuda. >>> vllm.__version__ '0.7.2' ``` ### 🐛 Describe the bug Hi, It looks like Qwen models can generate tokens out of vocabulary. We can see this...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Qwen/Qwen2.5-1.5B-Instruct generates out of vocabulary tokens bug;stale ### Your current environment ```python >>> import vllm INFO 02-12 20:27:04 __init__.py:190] Automatically detected platform cuda. >>> vllm._...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: ption: `Token id 151779 is out of vocabulary`. Here is a minimal code to reproduce this error. ```python import vllm from transformers import AutoTokenizer import numpy as np PROMPT = """ system Please reason step by st...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: Qwen/Qwen2.5-1.5B-Instruct generates out of vocabulary tokens bug;stale ### Your current environment ```python >>> import vllm INFO 02-12 20:27:04 __init__.py:190] Automatically detected platform cuda. >>> vllm._...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
