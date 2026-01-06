/*
  # K-Julia Voice Agent - Call Logs Database

  1. New Tables
    - calls table with comprehensive call logging fields

  2. Security
    - Enable RLS on calls table
    - Add policies for authenticated users

  3. Indexes
    - Index on issue_category for faster filtering
    - Index on created_at for time-series queries
*/

CREATE TABLE IF NOT EXISTS calls (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  call_id text NOT NULL,
  call_type text NOT NULL DEFAULT 'Inbound',
  virtual_number text DEFAULT 'TOLL_FREE',
  issue_category text NOT NULL,
  status text NOT NULL DEFAULT 'Pending',
  escalated boolean DEFAULT false,
  citizen_feedback text DEFAULT 'Neutral',
  priority text DEFAULT 'Medium',
  duration integer DEFAULT 0,
  agent_type text DEFAULT 'AI',
  satisfaction_score numeric(2,1) DEFAULT 0.0,
  callback_requested boolean DEFAULT false,
  language text DEFAULT 'English',
  resolution_time integer DEFAULT 0,
  created_at timestamptz DEFAULT now()
);

ALTER TABLE calls ENABLE ROW LEVEL SECURITY;

CREATE POLICY "Allow public read access for analytics"
  ON calls
  FOR SELECT
  USING (true);

CREATE POLICY "Allow authenticated insert"
  ON calls
  FOR INSERT
  TO authenticated
  WITH CHECK (true);

CREATE POLICY "Allow authenticated update"
  ON calls
  FOR UPDATE
  TO authenticated
  USING (true)
  WITH CHECK (true);

CREATE INDEX IF NOT EXISTS idx_calls_category ON calls(issue_category);
CREATE INDEX IF NOT EXISTS idx_calls_created_at ON calls(created_at DESC);
CREATE INDEX IF NOT EXISTS idx_calls_status ON calls(status);
CREATE INDEX IF NOT EXISTS idx_calls_type ON calls(call_type);
