# vllm-project/vllm#16981: [Usage]: Customized model parameters on different devices

| 字段 | 值 |
| --- | --- |
| Issue | [#16981](https://github.com/vllm-project/vllm/issues/16981) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Customized model parameters on different devices

### Issue 正文摘录

### Your current environment ```text vllm==0.8.2 ``` ### How would you like to use vllm Hi, I want to do inference with vLLM with my customized SpeechLLM, which is consisted of WeNet Audio Encoder and Qwen2.5-7B LLM. I referred to the Qwen2Audio code in the 0.8.2 branch of the repository, and have currently set vllm’s loading parameters to `dtype=bf16` and `tp=1`. However, I’m getting an error in WeNet’s RelativePositionAttention: the parameters end up on different devices—`linear_pos` is on the GPU, but `pos_bias_u` and `pos_bias_v` are on the CPU. When I load the model with HF transformers, it's normal. ``` class RelPositionMultiHeadedAttention(MultiHeadedAttention): def __init__(self, n_head: int, n_feat: int, dropout_rate: float, query_bias: bool = True, key_bias: bool = True, value_bias: bool = True, use_sdpa: bool = False, n_kv_head: Optional[int] = None, head_dim: Optional[int] = None): """Construct an RelPositionMultiHeadedAttention object.""" super().__init__(n_head, n_feat, dropout_rate, query_bias, key_bias, value_bias, use_sdpa, n_kv_head, head_dim) # linear transformation for positional encoding self.linear_pos = nn.Linear(n_feat, n_feat, bias=False) # these two learn...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Usage]: Customized model parameters on different devices usage ### Your current environment ```text vllm==0.8.2 ``` ### How would you like to use vllm Hi, I want to do inference with vLLM with my customized SpeechLLM,...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: of the repository, and have currently set vllm’s loading parameters to `dtype=bf16` and `tp=1`. However, I’m getting an error in WeNet’s RelativePositionAttention: the parameters end up on different devices—`linear_pos`...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: are plain `nn.Parameter`. Does vllm treat `nn.Parameter` objects in a special way? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the botto...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ay? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: value_bias: bool = True, use_sdpa: bool = False, n_kv_head: Optional[int] = None, head_dim: Optional[int] = None): """Construct an RelPositionMultiHeadedAttention object.""" super().__init__(n_head, n_feat, dropout

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
