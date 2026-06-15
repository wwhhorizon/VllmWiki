# vllm-project/vllm#21824: [Bug]: Data parallel stucked

| 字段 | 值 |
| --- | --- |
| Issue | [#21824](https://github.com/vllm-project/vllm/issues/21824) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | cold_start |
| Operator 关键词 | cache;cuda;operator;sampling;triton |
| 症状 | build_error |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Data parallel stucked

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I run the data parallel code to speed up, but vllm got stucked. Below is part of my code. ```python def parse_args(): parser = argparse.ArgumentParser() parser.add_argument('--model_name_or_path', type=str, required=True) parser.add_argument('--input_path', type=str, required=True) parser.add_argument('--output_path', type=str, required=True) parser.add_argument('--n', type=int, default=5) parser.add_argument('--batch_size', type=int, default=8) parser.add_argument('--enable_thinking', action='store_true') parser.add_argument('--dp_master_ip', type=str, default='127.0.0.1') parser.add_argument('--dp_size', type=int, default=8) parser.add_argument('--tp_size', type=int, default=1) parser.add_argument('--node_size', type=int, default=1) parser.add_argument('--node_rank', type=int, default=0) parser.add_argument('--gpus_per_dp_rank', type=int, default=1) parser.add_argument( '--mode', type=str, default='think', choices=[ 'instruct', 'think', "cot", ] ) args = parser.parse_args() return args def extract_content( output: str, mode: str, seperator: str=' ' ): if mode == 'instruct': return None, output elif mode == 'cot': match_rewrite...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: for {cnt} prompts") if __name__ == "__main__": from multiprocessing import Process self_args = parse_args() output_dir = os.path.dirname(self_args.output_path) os.makedirs(output_dir, exist_ok=True) # Sample prompts. fi...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: # max_model_len=32768, # gpu_memory_utilization=0.9, dtype='bfloat16', ) convs = [] for sample in samples: convs.append([ { 'role': 'user', 'content': INSTRUCTION.format(query=sample['gold_passage'][0]['passag
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: rgs(): parser = argparse.ArgumentParser() parser.add_argument('--model_name_or_path', type=str, required=True) parser.add_argument('--input_path', type=str, required=True) parser.add_argument('--output_path', type=str,...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: Data parallel stucked bug;stale ### Your current environment ### 🐛 Describe the bug I run the data parallel code to speed up, but vllm got stucked. Below is part of my code. ```python def parse_args(): parser = a...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: return None, output elif mode == 'cot': match_rewrite = re.search(r"####\s*(.*)", output) if match_rewrite: rewrite = match_rewrite.group(1) return None, rewrite.strip() else: return None elif mode == 'think': pattern

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
