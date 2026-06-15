# vllm-project/vllm#883: Code llama output gibberish code.

| 字段 | 值 |
| --- | --- |
| Issue | [#883](https://github.com/vllm-project/vllm/issues/883) |
| 状态 | closed |
| 标签 |  |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Code llama output gibberish code.

### Issue 正文摘录

Test on this [https://huggingface.co/docs/transformers/main/model_doc/code_llama](https://huggingface.co/docs/transformers/main/model_doc/code_llama) Env: 1. model: `Code Llama 7b Instruct` 2. `vLLM` `main` branch 0.1.4 on [4b6f069](https://github.com/vllm-project/vllm/commit/4b6f069b6fbb4f2ef7d4c6a62140229be61c5dd3). 3. transformers: 4.33.0.dev0 (build from main branch on [960807f](https://github.com/huggingface/transformers/commit/960807f62e53676723ab8281019219864ef3db4d)) 4. torch_dtype=torch.float16 (my gpu doesn't support bfloat16) Generated text from `transformers`: ```Python def remove_non_ascii(s: str) -> str: """ Remove non-ASCII characters from a string. Args: s (str): The string to remove non-ASCII characters from. Returns: str: The string with non-ASCII characters removed. """ result = "" for c in s: if ord(c) str: """ Remove non-ASCII and space characters from a string. return result ``` Generated text from `vLLM`: ```python : def remove_non_ascii(s: str) -> str: """ return result : For comments """ Remove non ascii inplace of special characters from a given string."""" non ascii => blank space, punctuation""""""codepointpython| nap string""" in Python"""test_safe u""...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: /transformers/commit/960807f62e53676723ab8281019219864ef3db4d)) 4. torch_dtype=torch.float16 (my gpu doesn't support bfloat16) Generated text from `transformers`: ```Python def remove_non_ascii(s: str) -> str: """ Remov...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: Code llama output gibberish code. Test on this [https://huggingface.co/docs/transformers/main/model_doc/code_llama](https://huggingface.co/docs/transformers/main/model_doc/code_llama) Env: 1. model: `Code Llama 7b Instr...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: 4b6f069b6fbb4f2ef7d4c6a62140229be61c5dd3). 3. transformers: 4.33.0.dev0 (build from main branch on [960807f](https://github.com/huggingface/transformers/commit/960807f62e53676723ab8281019219864ef3db4d)) 4. torch_dtype=t...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: frequency_penalty=0.0, temperature=1.0, top_p=1.0, top_k=-1, use_beam_search=False, stop=[], ignore_eos=False, max_tokens=128, logprobs=None), prompt token ids: [1, 822, 3349, 29918, 5464, 29918, 294, 18869, 29898, 2987...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: ncy_penalty=0.0, temperature=1.0, top_p=1.0, top_k=-1, use_beam_search=False, stop=[], ignore_eos=False, max_tokens=128, logprobs=None), prompt token ids: [1, 822, 3349, 29918, 5464, 29918, 294, 18869, 29898, 29879, 299...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
