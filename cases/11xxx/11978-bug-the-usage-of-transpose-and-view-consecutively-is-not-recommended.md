# vllm-project/vllm#11978: [Bug]: The usage of .transpose() and .view() consecutively is not recommended.

| 字段 | 值 |
| --- | --- |
| Issue | [#11978](https://github.com/vllm-project/vllm/issues/11978) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;hardware_porting;model_support;multimodal_vlm |
| 子分类 |  |
| Operator 关键词 | attention;cuda;operator |
| 症状 | build_error;import_error |
| 根因提示 | env_dependency;memory_layout;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug]: The usage of .transpose() and .view() consecutively is not recommended.

### Issue 正文摘录

### Your current environment \ ### Model Input Dumps _No response_ ### 🐛 Describe the bug ### Description We encountered the following error while running `internvl`: ``` view size is not compatible with input tensor's size and stride (at least one dimension spans across two contiguous subspaces). Use .reshape(...) instead. ``` After careful analysis, we found that this was a logic bug that had nothing to do with the device we were using. The issue occurs in the following line of code in `vllm/vllm/model_executor/models/intern_vit.py`: ```python class InternSdpaAttention(nn.Module): def forward(self, x): B, N, C = x.shape qkv = self.qkv(x) q, k, v = qkv.chunk(3, dim=-1) q = q.view(B, N, self.num_heads, self.head_dim) k = k.view(B, N, self.num_heads, self.head_dim) v = v.view(B, N, self.num_heads, self.head_dim) if self.qk_normalization: B_, N_, H_, D_ = q.shape q = self.q_norm.forward_native(q.flatten(-2, -1)).view(B_, N_, H_, D_) k = self.k_norm.forward_native(k.flatten(-2, -1)).view(B_, N_, H_, D_) q = q.transpose(1, 2) k = k.transpose(1, 2) v = v.transpose(1, 2) x = F.scaled_dot_product_attention(q, k, v, scale=self.scale) x = x.transpose(1, 2).view(B, N, -1) ``` ### Analysis A...

## 现有链接修复摘要

#8880 [Bugfix] fix #8630 | #9560 Fix: MI100 Support By Bypassing Custom Paged Attention

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: rmine whether `xformers` is available: ```python try: from xformers import ops as xops USE_XFORMERS_OPS = True except ImportError: USE_XFORMERS_OPS = False ``` The execution brunch is different depending on the value of...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 4: internvl`: ``` view size is not compatible with input tensor's size and stride (at least one dimension spans across two contiguous subspaces). Use .reshape(...) instead. ``` After careful analysis, we found that this wa...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: secutively is not recommended. bug ### Your current environment \ ### Model Input Dumps _No response_ ### 🐛 Describe the bug ### Description We encountered the following error while running `internvl`: ``` view size is...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: question occurs only when `USE_XFORMERS_OPS = False`, making it hard to reproduce under normal circumstances (e.g. use Nvidia GPU in most cases). **Why the usage of .transpose() and .view() consecutively is not recommen...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#8880](https://github.com/vllm-project/vllm/pull/8880) | mentioned | 0.45 | [Bugfix] fix #8630 | however, since pr #9560 was believed to have solved this problem, pr #8880 was closed. we found that this issue was not actually resolved in pr #9560, so we are submitting this ne… |
| [#9560](https://github.com/vllm-project/vllm/pull/9560) | mentioned | 0.45 | Fix: MI100 Support By Bypassing Custom Paged Attention | was closed. we found that this issue was not actually resolved in pr #9560, so we are submitting this new issue with our analysis and an explanation based on the official pytorch… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
