# vllm-project/vllm#4975: [Bug]: :vllm-0.4.2  pagedattention running error 

| 字段 | 值 |
| --- | --- |
| Issue | [#4975](https://github.com/vllm-project/vllm/issues/4975) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;ci_build |
| 子分类 | install |
| Operator 关键词 | attention;cuda;kernel;operator |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: :vllm-0.4.2  pagedattention running error 

### Issue 正文摘录

### Your current environment docker vllm/vllm-openai:v0.4.2 ### 🐛 Describe the bug Modify vllm's pagedattention and add a new parameter： attention_kernels.cu void paged_attention_v1( torch::Tensor& out, // [num_seqs, num_heads, head_size] torch::Tensor& query, // [num_seqs, num_heads, head_size] torch::Tensor& key_cache, // [num_blocks, num_heads, head_size/x, block_size, x] torch::Tensor& value_cache, // [num_blocks, num_heads, head_size, block_size] **torch::Tensor& value_cache_score, // [num_blocks, num_heads, head_size, block_size]** int num_kv_heads, // [num_heads] float scale, torch::Tensor& block_tables, // [num_seqs, max_num_blocks_per_seq] torch::Tensor& seq_lens, // [num_seqs] int block_size, int max_seq_len, const c10::optional & alibi_slopes, const std::string& kv_cache_dtype, float kv_scale) { ...... } ops.h oid paged_attention_v1( torch::Tensor& out, torch::Tensor& query, torch::Tensor& key_cache, torch::Tensor& value_cache, **torch::Tensor& value_cache_score,** int num_kv_heads, float scale, torch::Tensor& block_tables, torch::Tensor& context_lens, int block_size, int max_context_len, const c10::optional & alibi_slopes, const std::string& kv_cache_dtype, float kv_sc...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: 2 pagedattention running error bug;stale ### Your current environment docker vllm/vllm-openai:v0.4.2 ### 🐛 Describe the bug Modify vllm's pagedattention and add a new parameter： attention_kernels.cu void paged_attention...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: , block_size]** int num_kv_heads, // [num_heads] float scale, torch::Tensor& block_tables, // [num_seqs, max_num_blocks_per_seq] torch::Tensor& seq_lens, // [num_seqs] int block_size, int max_seq_len, const c10::optiona...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: um_seqs, num_heads, head_size] torch::Tensor& key_cache, // [num_blocks, num_heads, head_size/x, block_size, x] torch::Tensor& value_cache, // [num_blocks, num_heads, head_size, block_size] **torch::Tensor& value_cache_...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: =========== FAILED tests/kernels/test_attention.py::test_paged_attention[cuda:0-0-auto-dtype0-16-False-64-num_heads0-7-v1] - TypeError: paged_attention_v1() takes 13 positional arguments but 14 were given When compiling...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: then ,python3 setup.py develop copying build/lib.linux-x86_64-3.10/vllm/_moe_C.cpython-310-x86_64-linux-gnu.so -> vllm copying build/lib.linux-x86_64-3.10/vllm/_C.cpython-310-x86_64-linux-gnu.so -> vllm Creating /usr/lo...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
