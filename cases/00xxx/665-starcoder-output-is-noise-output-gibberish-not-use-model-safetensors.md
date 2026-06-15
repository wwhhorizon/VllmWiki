# vllm-project/vllm#665: Starcoder output is noise (output gibberish) ( not use model.safetensors)

| 字段 | 值 |
| --- | --- |
| Issue | [#665](https://github.com/vllm-project/vllm/issues/665) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Starcoder output is noise (output gibberish) ( not use model.safetensors)

### Issue 正文摘录

```py from vllm import LLM, SamplingParams model_path = "starcoderbase-1b" llm = LLM(model_path) sampling_params = SamplingParams(temperature=0, top_p=1, best_of=1, top_k=-1) text = "def main():" output = llm.generate(text, use_tqdm=False) print(output[0].outputs[0].text) ``` got the gibberish outpus: ```text "$GETEventArgs images (as (col-% http= http ```

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: is noise (output gibberish) ( not use model.safetensors) ```py from vllm import LLM, SamplingParams model_path = "starcoderbase-1b" llm = LLM(model_path) sampling_params = SamplingParams(temperature=0, top_p=1, best_of=...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: , top_k=-1) text = "def main():" output = llm.generate(text, use_tqdm=False) print(output[0].outputs[0].text) ``` got the gibberish outpus: ```text "$GETEventArgs images (as (col-% http= http ```
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: Starcoder output is noise (output gibberish) ( not use model.safetensors) ```py from vllm import LLM, SamplingParams model_path = "starcoderbase-1b" llm = LLM(model_path) sampling_params = SamplingParams(temperature=0,...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
